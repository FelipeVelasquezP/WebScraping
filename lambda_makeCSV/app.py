from datetime import datetime, timedelta
import csv
import urllib.request
from io import StringIO
import json
import boto3
import os
# from bs4 import BeautifulSoup
import requests
import csv


def handler(event,context):
    print('Hello Here')
    return{
        "statusCode":200,
        "body":json.dumps("Hello from Lambda")}