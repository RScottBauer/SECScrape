# -*- coding: utf-8 -*-
"""
Script for downloading indexes from SEC website and putting them into files
"""

import os
import urllib3

urllib3.disable_warnings()

years = []
quarters = ["QTR1","QTR2","QTR3","QTR4"]

for x in range(1993,2020):
    years.append(str(x))

print(years)
print(quarters)
    
http = urllib3.PoolManager()

def index_paths(year,quarter):
    for x in year:
        indexpath = 'E:/SEC/Indexes/Full/' + x
        if not os.path.exists(indexpath):
            os.makedirs(indexpath)
        for q in quarter:
            indexpathq = 'E:/SEC/Indexes/Full/' + x + '/' + q
            if not os.path.exists(indexpathq):
                os.makedirs(indexpathq)

def get_index_full(year,quarter):
    for y in year:
        yearurl = 'http://www.sec.gov/Archives/edgar/full-index/' + y
        for qs in quarter:
            fullurl = yearurl + '/' + qs + '/master.idx'
            fullr = http.request('GET', fullurl)
            filepath = 'E:/SEC/Indexes/Full/' + y + '/' + qs + '/' + y + qs + '.txt'
            file = open(filepath, 'wb')
            file.write(fullr.data)
            file.close()
    

index_paths(years,quarters)
get_index_full(years,quarters)


print('Done')