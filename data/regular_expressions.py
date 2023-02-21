from pyspark.sql import functions as f

covid_file_path = "/databricks-datasets/COVID/coronavirusdataset/PatientInfo.csv"
covid_df  = spark.read.format("csv")\
        .option("header",True)\
        .option("inferSchema", True)\
        .load(covid_file_path)

# display(covid_df) databricks command
covid_df.printSchema()

covid_df.select(f.regexp_replace(f.col("infection_case"), "patient", "PATIENT"),f.col("infection_case")).show(10)
# +---------------------------------------------------+--------------------+
# |regexp_replace(infection_case, patient, PATIENT, 1)|      infection_case|
# +---------------------------------------------------+--------------------+
# |                                    overseas inflow|     overseas inflow|
# |                                    overseas inflow|     overseas inflow|
# |                               contact with PATIENT|contact with patient|
# |                                    overseas inflow|     overseas inflow|
# |                               contact with PATIENT|contact with patient|
# |                               contact with PATIENT|contact with patient|
# |                               contact with PATIENT|contact with patient|
# |                                    overseas inflow|     overseas inflow|
# |                                    overseas inflow|     overseas inflow|
# |                               contact with PATIENT|contact with patient|
# +---------------------------------------------------+--------------------+


covid_df.select(f.regexp_extract(f.col("infection_case"), "patient" ,0).alias("extracted"),f.col("infection_case")).show(10)
# +---------+--------------------+
# |extracted|      infection_case|
# +---------+--------------------+
# |         |     overseas inflow|
# |         |     overseas inflow|
# |  patient|contact with patient|
# |         |     overseas inflow|
# |  patient|contact with patient|
# |  patient|contact with patient|
# |  patient|contact with patient|
# |         |     overseas inflow|
# |         |     overseas inflow|
# |  patient|contact with patient|
# +---------+--------------------+

contains_church = f.instr(f.col("infection_case"), "Church") >= 1
contains_hospital = f.instr(f.col("infection_case"), "Hospital") >= 1
covid_df.withColumn("infection_case_church_hospital", contains_church | contains_hospital)\
.select("infection_case", "infection_case_church_hospital").collect()