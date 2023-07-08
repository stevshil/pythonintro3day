#!/usr/bin/env python

import json
jsonInput=open("myEmployees.json","r")
jsonEmployees = json.load(jsonInput)
jsonInput.close()
print(jsonEmployees)
# Proof of dictionary
print(jsonEmployees["Steve"]["Role"])