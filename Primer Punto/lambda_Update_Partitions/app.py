import json
import boto3

def handler(event, context):
    print('Funciono el disparador')
    client = boto3.client('athena')
    queryStart = client.start_query_execution(
    QueryString = 'MSCK REPAIR TABLE acciones',
    QueryExecutionContext = {
        'Database': 'yahooscraping'
    }, 
    ResultConfiguration = { 'OutputLocation': 's3://bigdata99/logs/'})

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }