#!/usr/bin/env python

import csv
from pprint import PrettyPrinter

inData = open("dormantcos.csv","r")

# We'll use this dictionary to store all the other dictionaries by "Company Name"
allData={}

for line in csv.DictReader(inData):
    # line contains a dictionary version of the data using the 1st line of the file as the keys
    allData[line['Company Name']]=line

# print(allData)
pp=PrettyPrinter(indent=2, depth=6)
pp.pprint(allData)

inData.close()