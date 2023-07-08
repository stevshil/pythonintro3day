#!/usr/bin/env python

import requests
from pprint import PrettyPrinter

# Get UK Bank Holidays

# Make the request
webreq = requests.get("https://www.gov.uk/bank-holidays.json")

# Check we were successful, 200 OK
if webreq.status_code == 200:
    pp=PrettyPrinter(depth=6)
    pp.pprint(webreq.json())
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))
