from datetime import datetime, timedelta
import csv
import urllib.request
from io import StringIO
import json
import boto3
import os

def handler(event,context):
    print('Hello from zappa')
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
        urllib.request.urlretrieve(url,f"/tmp/{company}")
        urlSave=f'stocks/company={company}/year={yesterday.year}/month={yesterday.month}/day={yesterday.day}/Acciones_{company}.csv'
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(f'/tmp/{company}', 'yahoofinancescrapingpunto1',urlSave)        

    return{
        "statusCode":200,
        "body":json.dumps("Hello from Lambda")
    }