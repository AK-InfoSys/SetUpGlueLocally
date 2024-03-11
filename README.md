# SetUpGlueLocally
How to set up aws glue in your system to access. Full process


Installation of PySpark (All operating systems)
This tutorial will demonstrate the installation of PySpark and hot to manage the environment variables in Windows, Linux, and Mac Operating System.


1. Windows Installation
2. Linux Installation
3. Mac Installation

# **Pyspark = Python + Apache Spark**

Apache Spark is a new and open-source framework used in the big data industry for real-time processing and batch processing. It supports different languages, like Python, Scala, Java, and R.

Apache Spark is initially written in a Java Virtual Machine(JVM) language called Scala, whereas Pyspark is like a Python API which contains a library called Py4J. This allows dynamic interaction with JVM objects.

# **Windows Installation**
The installation which is going to be shown is for the Windows Operating System. It consists of the installation of Java with the environment variable and Apache Spark with the environment variable.

The recommended pre-requisite installation is Python, which is done from here.

### **Java installation**

* Go to Download Java JDK.
* Visit Oracle's website for the download of the Java Development Kit(JDK).

* Move to download section consisting of operating system Windows, and in my case, it's Windows Offline(64-bit). The installer file will be downloaded.Java installation

* Open the installer file, and the download begins.Java installation

* Go to "Command Prompt" and type "java -version" to know the version and know whether it is installed or not.Java installation

**Add the Java pathJava installation**

* Go to the search bar and "EDIT THE ENVIRONMENT VARIABLES.Java installation
* Click into the "Environment Variables'Java installation
* Click into "New" to create your new Environment variable.Java installation
* Use Variable Name as "JAVA_HOME' and your Variable Value as 'C:\Program Files (x86)\Java\jdk1.8.0_251'. This is your location of the Java file. Click 'OK' after you've finished the process.Java installation
* Let's add the User variable and select 'Path' and click 'New' to create it.Java installation
* Add the Variable name as 'PATH' and path value as 'C:\Program Files (x86)\Java\jdk1.8.0_251\bin', which is your location of Java bin file. Click 'OK' after you've finished the process.Java installation

##### Note: You can locate your Java file by going to C drive, which is C:\Program Files (x86)\Java\jdk1.8.0_251' if you've not changed location during the download.Java installation

**Installing Pyspark**
* Head over to the Spark homepage.

* Select the Spark release and package type as following and download the .tgz file.

* Installing PysparkInstalling Pyspark

#### **You can make a new folder called 'spark' in the C directory and extract the given file by using 'Winrar', which will be helpful afterward.**

* Download and setup winutils.exe
* Go to Winutils choose your previously downloaded Hadoop version, then download the winutils.exe file by going inside 'bin'. The link to my Hadoop version is: https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/winutils.exe

* Make a new folder called 'winutils' and inside of it create again a new folder called 'bin'.Then put the file recently download 'winutils' inside it.

* Environment variables
* Let's create a new environment where variable name as "hadoop_home" and variable value to be the location of winutils, which is "C:\winutils" and click "OK".
* Environment variables For spark, also let's create a new environment where the variable name is "Spark_home" and the variable value to be the location of spark, which is "C:\spark" and click "OK".
Environment variables
* Finally, double click the 'path' and change the following as done below where a new path is created "%Spark_Home%\bin' is added and click "OK".
* Environment variables
Finalizing Pyspark Installation
* Open Command Prompt and type the following command.
Finalizing Pyspark Installation
* Once everything is successfully done, the following message is obtained.
Finalizing Pyspark Installation
# **Linux Installation**
The installation which is going to be shown is for the Linux Operating System. It consists of the installation of Java with the environment variable along with Apache Spark and the environment variable.

The recommended pre-requisite installation is Python, which is done from here.

### **Java installation**
* Go to Download Java JDK.
* Visit Oracle's website for the download of the Java Development Kit (JDK).

* Move to the download section consisting of the operating system Linux and download it according to your system requirement.
Java Installation
* Save the file and click "Ok" to save in your local machine.
Java Installation
* Go to your terminal and check the recently downloaded file using 'ls' command.
Java Installation
* Install the package using the following command, which will install the debian package of java, which is recently downloaded.Java Installation
* Finally, you can check your java version using 'java --version' command.
Java Installation
* For configuring environment variables, let's open the 'gedit' text editor using the following command.
Java Installation
* Let's make the change by providing the following information where the 'Java' path is specified.
Java Installation
* To make a final change, let's type the following command.Java Installation
Installing Spark
* Head over to the Spark homepage.
* Select the Spark release and package type as following and download the .tgz file.Installing Spark
Installing Spark
* Save the file to your local machine and click 'Ok'.
Installing Spark
* Open your terminal and go to the recently downloaded file.
Installing Spark
* Let's extract the file using the following command.
Installing Spark
* After extracting the file, the new file is created and shown using the list('ls') command.
Installing Spark
* Configuring Environment Variable in Linux
* Let's open the 'bashrc' file using 'vim editor' by the command 'vim ~/.bashrc'.
* Configuring Environment Variable in Linux
* Provide the following information according to your suitable path on your computer. In my case, the following were the required path to my Spark location, Python path, and Java path. Also, first press 'Esc' and then type ":wq" to save and exit from vim.
* Configuring Environment Variable in Linux
* To make a final change, save, and exit. This results in accessing the pyspark command everywhere in the directory.Configuring Environment Variable in Linux
* Open pyspark using 'pyspark' command, and the final message will be shown as below.Configuring Environment Variable in LinuxConfiguring Environment Variable in Linux

# **Mac Installation**
**The installation which is going to be shown is for the Mac Operating System. It consists of the installation of Java with the environment variable along with Apache Spark and the environment variable.**

* The recommended pre-requisite installation is Python, which is done from here.

### **Java installation**
* Go to Download Java JDK.
* Visit Oracle's website for the download of the Java Development Kit (JDK).

* Move to download section consisting of the operating system Linux and download according to your system requirement.
Java Installation
* The installation of Java can be confirmed by using $java --showversion in the Terminal.
Installing Apache Spark
* Head over to the Spark homepage.
* Select the Spark release and package type as following and download the .tgz file.Installing Apache Spark
Installing Apache Spark
* Save the file to your local machine and click 'Ok'.
* Let's extract the file using the following command.
* $ tar -xzf spark-2.4.6-bin-hadoop2.7.tgz
* Configuring Environment Variable for Apache Spark and Python
* You need to open the ~/.bashrc or ~/.zshrc file depending upon your current Mac version.


###### export SPARK_HOME="/Downloads/spark"

###### export PATH=$SPARK_HOME/bin:$PATH

###### export PYSPARK_PYTHON=python3

###  OpenAI

Open pyspark using 'pyspark' command, and the final message will be shown as below.Configuring Environment Variable for Apache Spark and Python

#### Congratulations, you have made it to the end of this tutorial!

In this tutorial, you've learned about the installation of Pyspark, starting the installation of Java along with Apache Spark and managing the environment variables in Windows, Linux, and Mac Operating System.


### **~~For further Reference~~**
1. https://www.youtube.com/watch?v=j8AcYWQuv-M
2. https://www.youtube.com/watch?v=Rz-u0RExZtg&t=35s

# **For MongoDB Connector**

https://github.com/mongodb/mongo-spark?tab=readme-ov-file




