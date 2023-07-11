#!/usr/bin/env python

import requests, json
from pprint import PrettyPrinter

# Validate JSON
csvdata="""
a,b,c,d
e,f,g,h"""

mydata=json.dumps({"csv": csvdata})
print(mydata)

webreq = requests.post("http://localhost:8080/api/chkcsv", json=mydata)

# Check we were successful, 200 OK
if webreq.status_code == 200:
    pp=PrettyPrinter(depth=6)
    pp.pprint(webreq.json())
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))