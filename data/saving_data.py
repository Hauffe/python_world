file_path = 'dbfs:/databricks-datasets/atlas_higgs/atlas_higgs.csv'

data = spark.read\
  .option('header', True)\
  .csv(file_path)

data.write.mode('Overwrite').parquet(f'{working_directory}/atlas_parquet') # can be parquet, json, csv