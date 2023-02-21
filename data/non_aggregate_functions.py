from pyspark.sql import functions as f

df.take(1) # array of first row

v2 = df.take(5) # array of the first 5 rows

df.select(f.col("state")).na.replace("released","Released").show() # na finds null places, replace using the replace() func

# Create a dataframe
df4 = spark.createDataFrame([ (["a", "b", "c"],[1,2],), ([],[3,]) ], ['data','integers'])
display(df4)
# +---------+--------+
# |     data|integers|
# +---------+--------+
# |[a, b, c]|  [1, 2]|
# |       []|     [3]|
# +---------+--------+


# search it
df4.select(f.array_contains('data', '')).show()
# +----------------------+
# |array_contains(data, )|
# +----------------------+
# |                 false|
# |                 false|
# +----------------------+


df4.select(f.array_contains('data', 'b')).show()

# +-----------------------+
# |array_contains(data, b)|
# +-----------------------+
# |                   true|
# |                  false|
# +-----------------------+

