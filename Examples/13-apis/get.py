#!/usr/bin/env python

import requests
from pprint import PrettyPrinter

# Add 2 numbers
webreq = requests.get("http://localhost:8080/api/add/3/4")

# Check we were successful, 200 OK
if webreq.status_code == 200:
    pp=PrettyPrinter(depth=6)
    pp.pprint(webreq.json())
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))