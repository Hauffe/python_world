# Dataset: /databricks-datasets/learning-spark-v2/mnm_dataset.csv
# Scenario: What is the probability that a state gets greater than 55 blue MnM candy on average ?
# Steps:

# Read mnm dataset from following path: "/databricks-datasets/learning-spark-v2/mnm_dataset.csv"
# Count distinct states (count_states)
# Filter the records by color of the MnM (Blue), group by state and then calculate average MnM count
# Filter again where "average_count" > 55 and count the number of records (count_states_w_gt_55_blue_mnm)
# Calculate (count_states_w_gt_55_blue_mnm)/(count_states)


from pyspark.sql.functions import col, avg

mnm_path = '/databricks-datasets/learning-spark-v2/mnm_dataset.csv'
mnm_data =  spark.read\
  .option('inferSchema', False)\
  .option('header', True)\
  .csv(mnm_path)

mnm_distinct = mnm_data.select('State').distinct().count()
print(f"count of states: {mnm_distinct}")

mnm_data_filter = mnm_data.filter(col('Color') == "Blue")
mnm_data_agg = mnm_data_filter.groupBy(col('State')).agg(avg(col("Count")).alias('average_count'))
mnm_data_count = mnm_data_agg.filter(col('average_count')>55).count()
print(f"Aggragate: {mnm_data_count}")

probability = mnm_data_count / mnm_distinct
print(f"Probability: {probability}")