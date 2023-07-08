#!/usr/bin/env python

import requests
import datetime

# Get UK Bank Holidays

# Make the request.
webreq = requests.get("https://www.gov.uk/bank-holidays.json")

# Check we were successful, 200 OK
if webreq.status_code == 200:
    myhols = webreq.json()    
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))

mydata={}
for keys in myhols:
    # Extract only England and Wales holidays
    if "england-and-wales" in keys:
        mydata=myhols[keys]["events"]
        break

# Now we want only Easter Monday, Chirstmas Day and Boxing Day
for info in mydata:
    for key in info:
        if info[key] in ("Easter Monday", "Christmas Day", "Boxing Day"):
            # Split the api date into a list for the datetime module to create a date
            mapdate=map(int,info["date"].split("-"))
            mydate = datetime.date(*mapdate)
            print(info['title']+" is "+mydate.strftime("%A %d %B %Y"))