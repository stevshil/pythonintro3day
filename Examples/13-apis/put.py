#!/usr/bin/env python

import requests, json
from pprint import PrettyPrinter

# Validate JSON
mydataDict={"num": 5}
mydata=json.dumps(mydataDict)
webreq = requests.put("http://localhost:8080/api/global", json=mydata)

# Check we were successful, 200 OK
if webreq.status_code == 200:
    pp=PrettyPrinter(depth=6)
    pp.pprint(webreq.json())
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))