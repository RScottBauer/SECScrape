# -*- coding: utf-8 -*-
"""
Script for taking SEC indexes and downloading the associated forms then placing the meta data for those forms in a MongoDB database
"""

import pandas as pd

df = pd.read_csv("E:/SEC/Indexes/Testing/1999QTR3.txt",'|',header = None, names = [1,2,3,4,5], skiprows = 11)

