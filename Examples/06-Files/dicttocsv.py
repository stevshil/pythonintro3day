#!/usr/bin/env python

# List of lists dumped to CSV
orgs = [
    {"Index": 2,"Organization Id": "ec094061FeaF7Bc","Name": "Walls-Mcdonald","Website": "http://arias-willis.net/","Country": "Lithuania","Employees": 8156},
    {"Index": 3,"Organization Id": "DAcC5dbc58946A7","Name": "Gregory PLC","Website": "http://www.lynch-hoover.net/","Country": "Tokelau","Employees": 6121},
    {"Index": 19,"Organization Id": "dD1612190b24B12","Name": "Ford-Rice","Website": "https://peterson-irwin.com/","Country": "Turks and Caicos Islands","Employees": 3038},
    {"Index": 32,"Organization Id": "cB9E22bCCEE7DF9","Name": "Kent PLC","Website": "https://www.mcconnell.com/","Country": "Netherlands","Employees": 6707}
]

# Use any list element to obtain the keys from one of the dictionary objects
header=orgs[0].keys()

# Open the CSV file for writing
csvOutput = open("myorgs.csv","w")

# Write the CSV file header first
csvOutput.write(",".join(header)+"\n")

# Write the rest of the data
for data in orgs:
    # Grab all values of the current dictionary and convert to a string list
    currentData = map(str,data.values())
    # Join the list into a string separated by , and write to file
    csvOutput.write(",".join(currentData)+"\n")

csvOutput.close()