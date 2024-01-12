import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from awsglue.dynamicframe import DynamicFrame ##Akhilesh

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

predicate_pushdown = "region in ('ca','gb','us')" ##Akhilesh

# Script generated for node Amazon S3
AmazonS3_node1705048340225 = glueContext.create_dynamic_frame.from_catalog(
    database = "de_youtube_raw", table_name = "raw_statistics", 
    transformation_ctx = "AmazonS3_node1705048340225", 
    push_down_predicate = predicate_pushdown
)
##Akhilesh push_down_predicate 

# Script generated for node Change Schema
ChangeSchema_node1705048815890 = ApplyMapping.apply(
    frame=AmazonS3_node1705048340225,
    mappings=[
        ("video_id", "string", "video_id", "string"),
        ("trending_date", "string", "trending_date", "string"),
        ("title", "string", "title", "string"),
        ("channel_title", "string", "channel_title", "string"),
        ("category_id", "string", "category_id", "bigint"),
        ("publish_time", "string", "publish_time", "string"),
        ("tags", "string", "tags", "string"),
        ("views", "string", "views", "bigint"),
        ("likes", "string", "likes", "bigint"),
        ("dislikes", "string", "dislikes", "bigint"),
        ("comment_count", "string", "comment_count", "bigint"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "string", "comments_disabled", "boolean"),
        ("ratings_disabled", "string", "ratings_disabled", "boolean"),
        ("video_error_or_removed", "string", "video_error_or_removed", "boolean"),
        ("description", "string", "description", "string"),
    ],
    transformation_ctx="ChangeSchema_node1705048815890",
)
#datasink1 = ChangeSchema_node1705048815890.toDF().coalesce(1)
#df_final_output = DynamicFrame.fromDF(datasink1, glueContext, "df_final_output")
# Script generated for node Amazon S3
AmazonS3_node1705048433029 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1705048815890,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://de-on-youtube-cleansed-us-east-1-dev-akprojectlearn/youtube/raw_statistics/",
    },
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1705048433029",
)

job.commit()
