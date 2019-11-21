# -*- coding: utf-8 -*-
"""
Yahoo Finance Rapid API Requests & insterting into MongoDB Database
"""

from pymongo import MongoClient
import requests
import json

client = MongoClient('localhost',27017)
db = client.hist
symbol = "SJNK"
underlying = "Barclays Capital US High Yield 350mn Cash Pay 0-5 Yr 2% Capped Index"
timestart = "1331731800"
timestop = "1574355600"

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"

querystring = {"frequency":"1d","filter":"history","period1":timestart,"period2":timestop,"symbol":symbol}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "a93deb9669msh6611a26605a8fe1p15899bjsn3547d415bfd7"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

entry = response.text
record = db.etf.insert_one(json.loads(entry))
recordid = record.inserted_id
recordadded = db.etf.update_one({"_id": recordid}, {"$set": {"symbol": symbol}})
recordaddedunder = db.etf.update_one({"_id": recordid}, {"$set": {"underlying": underlying}})

print(len(response.text))
print(symbol)
print(underlying)
print("Done")