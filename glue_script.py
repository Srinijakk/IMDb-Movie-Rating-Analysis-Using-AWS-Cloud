import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load data from S3
datasource = glueContext.create_dynamic_frame.from_catalog(database="imdb_db", table_name="imdb_raw")

# Clean and transform
transformed_df = datasource.toDF().dropna(subset=["IMDB_Rating", "Gross"]).withColumnRenamed("Series_Title", "Title")

# Load into Redshift
transformed_dyf = DynamicFrame.fromDF(transformed_df, glueContext, "transformed_dyf")
glueContext.write_dynamic_frame.from_options(
    frame=transformed_dyf,
    connection_type="redshift",
    connection_options={
        "url": "jdbc:redshift://your-redshift-cluster:5439/yourdb",
        "user": "username",
        "password": "password",
        "dbtable": "imdb_cleaned",
        "redshiftTmpDir": "s3://your-temp-dir/"
    }
)

job.commit()
