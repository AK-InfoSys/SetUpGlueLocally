from pymongo.common import alias
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, map_keys, map_values, regexp_extract, expr
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, MapType

spark = SparkSession. \
    builder. \
    appName("pyspark-notebook2"). \
    config("spark.executor.memory", "1g"). \
    config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1"). \
    config("spark.sql.mapKeyDedupPolicy", "LAST_WIN"). \
    config("spark.mongodb.read.connection.uri",
           "mongodb+srv://mumbaidevdsp:4z6XaZlfWxvRXZ9g@npsdevdb.iqqr8.mongodb.net/?tls=true"). \
    getOrCreate()

mongo_uri = "mongodb+srv://mumbaidevdsp:4z6XaZlfWxvRXZ9g@npsdevdb.iqqr8.mongodb.net/npsdevdb."

user_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", mongo_uri + "users").load()
survey_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", mongo_uri + "surveys").load()
user_tracking_map_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri",
                                                                                       mongo_uri + "userTrackingMap").load()
survey_response_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri",
                                                                                     mongo_uri + "surveyResponse").load()

user_df.createOrReplaceTempView("users_df")
survey_df.createOrReplaceTempView("survey_df")
user_tracking_map_df.createOrReplaceTempView("user_tracking_map_df")
survey_response_df.createOrReplaceTempView("survey_response_df")

# survey_df.show()
# user_tracking_map_df.show()
# survey_response_df.show()


npsSchema = StructType([
    StructField("_id", StringType()),
    StructField("uhid", StringType()),
    StructField("trackingIdResponseMap", MapType(
        StringType(),
        StructType([
            StructField("$id", StringType())
        ])
    )),
])

user_df = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", mongo_uri + "users") \
    .schema(npsSchema).load()

print("user_df")
user_df.show(5, False)

for row in survey_df.collect():
    surveyId = row["_id"]
    try:

        exploded_df = user_df.select("uhid", explode(map_values("trackingIdResponseMap")).alias("trackingIdResponse"))

        # exploded_df = user_df.select(
        #     "uhid",
        #     explode("trackingIdResponseMap").alias("trackingIdResponse")
        # ).filter(col("trackingIdResponse.surveyId") == surveyId)

        # # Perform the join operation
        # joined_df = exploded_df.join(
        #     user_tracking_map_df,
        #     exploded_df["trackingIdResponse"] == user_tracking_map_df["_id"],
        #     "inner"
        # )
        print("exploded_df")
        exploded_df.show(5, False)
        break
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        pass
