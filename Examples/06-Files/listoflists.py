#!/usr/bin/env python

# Data set from
# https://www.datablist.com/learn/csv/download-sample-csv-files

# The headers
header=["Index","Organization Id","Name","Website","Country","Description","Founded","Industry","Number of employees"]

# List of lists dumped to CSV
orgs = [
    [2,"ec094061FeaF7Bc","Walls-Mcdonald","http://arias-willis.net/","Lithuania","Compatible encompassing groupware",2005,"Utilities",8156],
    [3,"DAcC5dbc58946A7","Gregory PLC","http://www.lynch-hoover.net/","Tokelau","Multi-channeled intangible help-desk",2019,"Leisure / Travel",6121],
    [19,"dD1612190b24B12","Ford-Rice","https://peterson-irwin.com/","Turks and Caicos Islands","Sharable intangible leverage",1971,"Computer / Network Security",3038],
    [32,"cB9E22bCCEE7DF9","Kent PLC","https://www.mcconnell.com/","Netherlands","Reduced neutral knowledgebase",2005,"Civil Engineering",6707]
]

# Open the CSV file for writing
csvOutput = open("myorgs.csv","w")

# Write the CSV file header first
csvOutput.write(",".join(header)+"\n")

# Write the rest of the data
for data in orgs:
    # Turn all list elements into string so we can join with ,
    currentData = map(str,data)
    # Join the list into a string separated by , and write to file
    csvOutput.write(",".join(currentData)+"\n")

csvOutput.close()