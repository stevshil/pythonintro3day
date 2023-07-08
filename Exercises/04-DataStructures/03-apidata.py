#!/usr/bin/env python

# This example uses the https://dummyjson.com/todos API

import requests

urlresponse = requests.get('https://dummyjson.com/todos')
data=urlresponse.json()
