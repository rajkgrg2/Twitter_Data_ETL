# Twitter_Data_ETL_Pipeline_Airflow_EC2_S3

This project is about extracting data from Twitter API, using Python scripts, design ETL automated scheduled pipelines using Airflow which is running on AWS EC2 and load data into S3 bucket for further analysis.

# Toolkit
- Tweepy
- Apache Airflow
- Pandas Library
- Python
- AWS EC2
- AWS S3

![Twitter_ETL](https://user-images.githubusercontent.com/7123198/230835468-2ff72e44-86f6-4a45-9741-a86849111982.png)

- TWitter APi is used to collect data from specific twitter account with help of Python script.
- Collected unstructured data from Twitter API is saved to locally.
- Apache Airflow and required dependencys are downloded in AWS EC2.
- ETL job is created in Airflow with python script and data is loaded to S3 bucket.



# Unstructured CSV file extracted from twitter API.
![csv](https://user-images.githubusercontent.com/7123198/230835800-909ce06a-4c36-4dce-a011-61459661ca91.png)



# Cleaned data ready to use for further analysis.

![cleaned_tweet_Tech_Impact](https://user-images.githubusercontent.com/7123198/231534976-fdcda727-5be6-446a-a118-a895d3a20261.png)
