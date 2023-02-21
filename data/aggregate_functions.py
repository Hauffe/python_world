from pyspark.sql import functions as f


fl = "/databricks-datasets/power-plant/data/Sheet1.tsv"
df = spark.read\
  .format('csv')\
  .option('inferSchema', True)\
  .option('header', True)\
  .option('delimiter', '\t')\
  .load(fl)

df.filter(f.col("AT")>14).count()

df.select(f.count("PE")).show()

df.select(f.sum("AT")).show()

df.select(f.min("AT"), f.max("AT")).show()

df.select(
  f.count("V"),
  f.min("V"),
  f.max("V"),
  f.mean("V").alias("mean()"),
  f.avg("V").alias("avg()"),
  f.expr("avg(V)").alias("expr(avg)"),
  f.expr("mean(V)").alias("expr(mean)")
  ).show()