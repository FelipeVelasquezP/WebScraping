from datetime import datetime, timedelta
import csv
import urllib.request
from io import StringIO
import json
import boto3



def handler(event,context):
    print('hello from Zappa')
    # current date and past dates
    today = datetime.now().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    yesterday = today - timedelta(days=1)
    yesterdayplus = today - timedelta(days=2)

    # timestamp of dates
    timestamp1 = round(datetime.timestamp(yesterdayplus))
    timestamp2 = round(datetime.timestamp(yesterday))

    # Array of companies
    companies = ["AVHOQ","EC","AVAL","CMTOY"]

            
    # Scraping to get csv
    for company in companies:
        url = f'https://query1.finance.yahoo.com/v7/finance/download/{company}?period1={timestamp1}&period2={timestamp2}&interval=1d&events=history&includeAdjustedClose=true'
        respuesta = urllib.request.urlopen(url)
        f = StringIO(bytearray(respuesta.read()).decode())
        archivo = csv.reader(f)
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file('/stocks','yahoofinancescrapingpunto1',archivo)

    return {
        'statusCode': 200,
        'body': json.dumps('Funciono!')
    }

