import pyspark.sql.functions as f

fire_incidents = "/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-incidents.csv"
fire_calls = "/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-calls.csv"


df_fire_incidents = spark.read\
  .format("csv")\
  .option("header", True)\
  .option("inferSchema", True)\
  .load(fire_incidents)\
  .filter(f.col('Incident Number').isNotNull())\
  .dropDuplicates(subset = ['Incident Number'])
df_fire_incidents.cache().display()

df_fire_calls = spark.read\
  .format("csv")\
  .option("header", True)\
  .option("inferSchema", True)\
  .load(fire_calls)\
  .filter(f.col('Incident Number').isNotNull())\
  .dropDuplicates(subset = ['Incident Number'])
df_fire_calls.cache()

# From df_fire_incidents filter all records where "Primary Situation" column has "False" as substring
# From df_fire_calls filter all records where "OrigPriority" is 3

primary_situation_false = df_fire_incidents.filter(f.lower(f.col("Primary Situation")).contains("false"))

orig_priority_3 = df_fire_calls.filter(f.col("OrigPriority")==3)

# Join the resultant coulmns and get a count
inner_join_df = orig_priority_3.alias("df1")\
  .join(
    primary_situation_false.alias("df2"), 
    f.col("df1.`Incident Number`") == f.col("df2.`Incident Number`"), 
    "inner"
  )
inner_join_df.count()


inner_join_df = orig_priority_3.join(
    primary_situation_false,
    "Incident Number",
    "inner"
  )