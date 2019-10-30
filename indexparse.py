# -*- coding: utf-8 -*-
"""
Script for taking SEC indexes and downloading the associated forms then placing the meta data for those forms in a MongoDB database
"""
import pymongo as py
from py import MongoClient
import pandas as pd

client = MongoClient('localhost',27017)
db = client.testbase


df = pd.read_csv("C:\\Users\\Robert Bauer\\Documents\\2015QTR1.txt",'|', header = None, names = [1,2,3,4,5], skiprows = 11)

print(df.shape[0])
print(type(df.iloc[0,1]))

def indexparser(indexframe):
    for row in range(indexframe.shape[0]):
        entry = {"CIK": indexframe.iloc[row,1],
                 "Company Name": indexframe.iloc[row,2],
                 "Form Type": indexframe.iloc[row,3],
                 "Date Filed": indexframe.iloc[row,4],
                 "Filename": indexframe.iloc[row,5]
             }
        record = db.test.insert_one(entry)
    return record;

print("Done")
