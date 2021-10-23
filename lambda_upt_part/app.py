import json
import boto3

def handler(event, context):
    client = boto3.client('athena')
    queryStart = client.start_query_execution(
    QueryString = 'MSCK REPAIR TABLE periodicos',
    QueryExecutionContext = {
        'Database': 'scrapingNews'
    }, 
    ResultConfiguration = { 'OutputLocation': 's3://bigdata99/logs/'})

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }