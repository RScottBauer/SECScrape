# -*- coding: utf-8 -*-
"""
Script for taking SEC indexes and downloading the associated forms then placing the meta data for those forms in a MongoDB database
"""
from pymongo import MongoClient
import pandas as pd
from datetime import date

client = MongoClient('localhost',27017)
db = client.sec
currentdate = [date.today().year,date.today().month]

def indexparser(indexframe):
    for row in range(indexframe.shape[0]):
        entry = {"CIK": int(indexframe.iloc[row,0]),
                 "Company Name": indexframe.iloc[row,1],
                 "Form Type": indexframe.iloc[row,2],
                 "Date Filed": indexframe.iloc[row,3],
                 "Filename": indexframe.iloc[row,4]
             }
        record = db.forms.insert_one(entry)
    return record;

def formyears (date):
    titles = []
    quarters = ["QTR1","QTR2","QTR3","QTR4"]
    for x in range(1993,date[0]):
        for qtr in quarters:
            titles.append([x,qtr])
            
    if date[1] < 4:
        titles.append([date[0],"QTR1"])
    elif date[1] < 7:
        titles.append([date[0],"QTR1"])
        titles.append([date[0],"QTR2"])
    elif date[1] < 10:
        titles.append([date[0],"QTR1"])
        titles.append([date[0],"QTR2"])
        titles.append([date[0],"QTR3"])
    else:
        titles.append([date[0],"QTR1"])
        titles.append([date[0],"QTR2"])
        titles.append([date[0],"QTR3"])
        titles.append([date[0],"QTR4"])
        
    return titles;

def dfmaker(dateslist):
    for dates in dateslist:
        dfs = pd.read_csv("E:/SEC/Indexes/Full/" + str(dates[0]) + "/" + dates[1] + "/" + str(dates[0]) + dates[1] + ".txt", '|', header = None, names = [1,2,3,4,5], skiprows = 11)
        indexparser(dfs)
    return None;

dfmaker(formyears(currentdate))
print("Done")
