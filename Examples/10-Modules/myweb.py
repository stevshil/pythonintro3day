#!/usr/bin/env python

import requests
from pprint import PrettyPrinter

# Get Star Wars planets from the API

# Make the request
webreq = requests.get("https://swapi.dev/api/planets/2/?format=json")

# Check we were successful, 200 OK
if webreq.status_code == 200:
    pp=PrettyPrinter(depth=6)
    pp.pprint(webreq.json())
else:
    print("We were unable to complete the request with "+repr(webreq.status_code))