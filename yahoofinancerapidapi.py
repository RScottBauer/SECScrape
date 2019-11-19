# -*- coding: utf-8 -*-
"""
Yahoo Finance Rapid API Requests & insterting into MongoDB Database
"""

from pymongo import MongoClient
import requests
import json

client = MongoClient('localhost',27017)
db = client.sec

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"

querystring = {"symbol": "GE"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "a93deb9669msh6611a26605a8fe1p15899bjsn3547d415bfd7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

entry = response.text
record = db.rapidapitest.insert_one(json.loads(entry))


print(response.text)
print(type(json.loads(entry)))
print("Done")