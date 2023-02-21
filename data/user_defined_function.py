from pyspark.sql.types import IntegerType, StringType


covid_file_path = "/databricks-datasets/COVID/coronavirusdataset/PatientInfo.csv"
covid_df  = spark.read.format("csv")\
        .option("header",True)\
        .option("inferSchema", True)\
        .load(covid_file_path)


def addOne(rec):
    return rec + 1

udf_fun = spark.udf.register('add1', addOne, IntegerType())
udf_fun


to_upper = udf(lambda s: s.upper(), StringType())

@udf
def t_year(t):
    if t is not None:
        return t.split("-")[0]

covid_df.select(
  to_upper(f.col("province")),
  t_year(f.col("symptom_onset_date"))
).show()



from pyspark.sql import functions as f
from pyspark.sql.types import StringType

@udf
def bucket_delay(rec):
  try:
    val = int(rec)
  except Exception as e:
    return rec
  option = None
  if val < 0:
    option = 0
  elif val == 0:
    option = 1
  elif val > 0:
    if val < 30:
      option = 2
    else:
      option = 3
  return option

# bucket_delay = spark.udf.register('bucket_delay', bucket_delay, StringType())   used to register if @udf is not above the function

df.select(
  col('ArrDelay'),
  bucket_delay(col('ArrDelay')).alias('bucket delay')
).show()



def fix_country(col: Column) -> Column:
  fixed_country = F.initcap(F.lower(F.trim(col)))
