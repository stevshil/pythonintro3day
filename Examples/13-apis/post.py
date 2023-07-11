#!/usr/bin/env python

import requests, json
from pprint import PrettyPrinter

# Validate JSON
mydataDict={"Name": "Steve", "Position": "Seated"}
mydata=json.dumps(mydataDict)
webreq = requests.post("http://localhost:8080/api/chkjson", json=mydata)

# Check we were successful, 200 OK
if webreq.status_code == 200:
    pp=PrettyPrinter(depth=6)
    pp.pprint(webreq.json())
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))