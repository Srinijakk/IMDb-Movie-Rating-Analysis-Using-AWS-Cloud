import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    response = glue.start_job_run(JobName='your_glue_job_name')
    print(f"Glue job started: {response['JobRunId']}")
    return {'statusCode': 200, 'body': 'ETL Job Triggered Successfully'}
