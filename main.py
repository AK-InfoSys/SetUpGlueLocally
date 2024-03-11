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
           "mongodb://localhost:27017/"). \
    getOrCreate()

mongo_uri = "mongodb://localhost:27017/dbNAME."

df1 = spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", mongo_uri + "collectionNAME").load()

df1.createOrReplaceTempView("users_df")


# survey_df.show()
# user_tracking_map_df.show()
# survey_response_df.show()


Schema = StructType([
    StructField("_id", StringType()),
    StructField("data", StringType()),
    StructField("map", MapType(
        StringType(),
        StructType([
            StructField("$id", StringType())
        ])
    )),
])


print("user_df")
df1.show(5, False)

for row in df1.collect():
    surveyId = row["_id"]
    try:

        exploded_df = df1.select("data", explode(map_values("map")).alias("mapResponse"))

        print("exploded_df")
        exploded_df.show(5, False)
        break
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        pass
