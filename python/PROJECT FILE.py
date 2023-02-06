'''
# How to  deal with correptd records
import pyspark
from pyspark.sql.types import *
# from pyspark.sql.functions import *
from pyspark.sql import SparkSession
sc = pyspark.SparkContext.getOrCreate()
spark=pyspark.sql.SparkSession(sc)
spark01=SparkSession.builder.appName("task1").master("local[2]").getOrCreate()
schema1=StructType([ StructField("article_id", IntegerType()),
                     StructField("title", StringType()),
                     StructField("short_desc", FloatType()),
                     StructField("article_desc", IntegerType()),
                     StructField("_corrupt_record", StringType())])
# data2 = spark01.read.schema(schema1).option("header","true").option("mode","DROPMALFORMED").csv("C:\\Users\\Pooja\\Downloads\\hive_school1.txt")
# data2.show()
# data2 = spark01.read.schema(schema1).option("header","true").option("badRecordsPath","C:\\Users\\DELL 5430\\Desktop\\New Folder\\badRecordsOrCorruptedRecordsFile").csv("C:\\Users\\DELL 5430\\Downloads\\hive_school1.txt")
data2 = spark01.read.schema(schema1).option("header","true").option("mode","PERMISSIVE").csv("C:\\Users\\Pooja\\Downloads\\hive_school1.txt").cache()

data2.show()

distinctDF = data2.distinct()
print("Distinct count: "+str(distinctDF.count()))
distinctDF.show(truncate=False)
df2 = data2.dropDuplicates()
print("Distinct count: "+str(df2.count()))
df2.show()
# df2.write.format("csv").option("header","true").save("C:\\spark_file\\duplicates")


from pyspark.sql.functions import col
data3=data2.where(col("_corrupt_record").isNull()).drop("_corrupt_record")
data4=data2.select(col("_corrupt_record")).where(col("_corrupt_record").isNotNull())
data3.show(truncate=False)
data4.show(truncate=False)
# data4.write.format("csv").option("header","true").save("C:\\spark_file\\duplicates")
'''






# with column example
'''from pyspark.sql.functions import col
data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
df = spark.createDataFrame(data=data, schema = columns)

# change datatype
df.withColumn("salary",col("salary").cast("Integer")).show()

# * salary  column by 100
df.withColumn("salary",col("salary")*100).show()

# add one more salary copy column
df.withColumn('copy',col('salary')* -1).show()

# drop copied column
df.drop("copy").show()

# rename saalary column with amount
df.withColumnRenamed("salary","amount").show()

# add  new column to table
from pyspark.sql.functions import lit
df.withColumn("Country", lit("USA")).show()
df.withColumn("Country", lit("")).withColumn("anotherColumn",lit("")) .show()
'''





'''
# PySpark Distinct to Drop Duplicate Rows

# Import pySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Prepare Data
data = [("James", "Sales", 3000), \
    ("Michael", "Sales", 4600), \
    ("Robert", "Sales", 4100), \
    ("Maria", "Finance", 3000), \
    ("James", "Sales", 3000), \
    ("Scott", "Finance", 3300), \
    ("Jen", "Finance", 3900), \
    ("Jeff", "Marketing", 3000), \
    ("Kumar", "Marketing", 2000), \
    ("Saif", "Sales", 4100) \
  ]

# Create DataFrame
columns= ["employee_name", "department", "salary"]
df = spark.createDataFrame(data = data, schema = columns)
df.printSchema()
# df.show(truncate=False)

#  Get Distinct Rows (By Comparing All Columns)
distinct=df.distinct().show()

# drop duplicates
df2=df.dropDuplicates().show()


# drop dupllicates on selected mulltiple columns
df3=df.dropDuplicates(["department","salary"]).show()
'''





# How to drop null values
# syntax;
# drop(how='any', thresh=None, subset=None)
# how – This takes values ‘any’ or ‘all’. By using ‘any’, drop a row if it contains NULLs on any columns. By using ‘all’, drop a row only if all columns have NULL values. Default is ‘any’.
# thresh – This takes int value, Drop rows that have less than thresh hold non-null values. Default is ‘None’.
# subset – Use this to select the columns for NULL values. Default is ‘None.


# df.na.drop().show(false)

# df.na.drop("any").show(false)

# df.na.drop("all").show(false)

# df.na.drop(subset=["population","type"]).show(truncate=False)

# df.dropna().show(truncate=False)
