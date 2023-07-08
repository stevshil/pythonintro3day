#!/usr/bin/env python

# This example uses the https://dummyjson.com/todos API

import requests

urlresponse = requests.get('https://dummyjson.com/todos')
data=urlresponse.json()

# Print the limit value of 30
print("Limit: "+str(data['limit']))

# Print the 12th todo
print("Todo 12: "+str(data["todos"][12]['todo']))

# Ask the user to enter a number from 1 to todos list length and store in userNum as an integer
userNum = int(input("Enter a number between 1 and "+str(len(data["todos"]))+": "))

# Now print the todo that the user has requested
print("Todo "+str(userNum)+": "+str(data["todos"][userNum]['todo']))

# Delete the skip key and value from the data
del data["skip"]

# Dump the dictionary to prove that the skip key has gone
print(data)