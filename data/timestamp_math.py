import pyspark.sql.functions as f

fire_incidents = "/databricks-datasets/learning-spark-v2/sf-fire/sf-fire-incidents.csv"

#Reading the dataset
df_fire_incidents = spark.read\
  .format("csv")\
  .option("header", True)\
  .option("inferSchema", True)\
  .load(fire_incidents)\
  .filter(f.col('Incident Number').isNotNull())\
  .dropDuplicates(subset = ['Incident Number'])

format_ = "MM/dd/yyyy hh:mm:ss a"

df_with_time_diff = df_fire_incidents.withColumn(
  "TimeTakenInMinutes",
  f.to_timestamp(f.col("Close DtTm"), format_).cast("long") - f.to_timestamp(f.col("Arrival DtTm"),format_).cast("long"))

sorted_df = df_with_time_diff.select(f.col("Incident Number"), f.col("Arrival DtTm"), f.col("Close DtTm"), f.col("TimeTakenInMinutes")/60).orderBy(f.desc("TimeTakenInMinutes"))

# display(sorted_df)