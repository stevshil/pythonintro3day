#!/usr/bin/env python

import json

# Create JSON string
jData = """[ { "inv-100": { "DueDate": "20230105", "Total": 1100.00,
  "Status": "Sent", "Lines": [ { "Description": "Drill", "Amount": 350.00,
  "Quantity": 2 }, { "Description": "Saw", "Amount": 400.00,
  "Quantity": 1 } ] } } ]"""

# JSON data loaded into Python Dictionary
invoice = json.loads(jData)

# Show invoice Total
print("Invoice total: "+str(invoice[0]["inv-100"]["Total"]))