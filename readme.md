  This project showcases how AWS can be used for Data Engineering for batch-processing structured data: AWS Glue, S3, Redshift, Athena and Lambda. Raw data from two sources (CSV and JSON) were uploaded to an S3 bucket using the S3 CLI client. AWS Glue was used to clean the .csv data and convert it to .parquet. After that, a Glue Crawler was created to Catalog the data. 

  An AWS lambda function was created to extract from the JSON data from an S3 bucket. The trigger to this function was any type of object creation in the S3 bucket that would store the JSON data. After extracting the data, another Glue Crawler would catalog the data in AWS Glue. 

  A Glue ETL job was created to perform a join on these two data set and store the final data in another S3 bucket. Throughout the entire process, AWS Athena was used to query the catalogued data and make sure the result data were in order and querying was smooth. Finally, the data was shifted to a Redshift warehouse from where it can be connected to a BI tool such as Power BI or Looker Studio.

Languages used: Python, SQL, bash.
