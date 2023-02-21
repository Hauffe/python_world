# Broadcast

from pyspark.sql import functions as f

count_credit_card_payers = large_df.alias('large').join(f.broadcast(small_df.alias('small')), f.col('large.payment_type')==f.col('small.payment_type')).filter(f.col("small.payment_desc") == 'Credit card').count()

print(count_credit_card_payers)


# View
temp_view = data.filter((f.col("cancellation_policy") == "flexible") | (f.col("review_scores_rating") > 90))
temp_view.createOrReplaceTempView('tempView')