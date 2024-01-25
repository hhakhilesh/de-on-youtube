![de_on_youtube](https://github.com/hhakhilesh/de-on-youtube/assets/141318384/a879798e-2d80-4f7a-a24b-5e7b10278125)
  This project showcases how AWS can be used for Data Engineering for batch-processing structured data: AWS Glue, S3, Redshift, Athena and Lambda. Raw data from two sources (CSV and JSON) were uploaded to an S3 bucket using the S3 CLI client. AWS Glue was used to clean the CSV data, partition it and save it in .parquet format. After that, a Glue Crawler was created to catalog this data. 

  An AWS lambda function was created to extract data from JSON files and save it into an S3 bucket. The trigger to this function was any type of object creation in the S3 bucket that would store the JSON data. After extracting the data, another Glue Crawler would catalog the data in AWS Glue. 

  A Glue ETL job was created to perform a join on these two datasets and store the final data in another S3 bucket. Throughout the entire process, AWS Athena was used to query the catalogued data and make sure the result data was in order and querying was smooth. Finally, the data was shifted to a Redshift warehouse from where it can be connected to a BI tool such as Power BI or Looker Studio.

Languages used: Python, SQL, bash.
