#!/usr/bin/env python

from os.path import exists

if not exists("taxrates.csv"):
    print("Tax rates file does not exist")
    exit()

taxratesIn = open("taxrates.csv","r")
# Grab the first element as it is the header
header=taxratesIn.readline()
# Read the rest of the data
taxRatesData=taxratesIn.readlines()
taxratesIn.close()

# We now have a list of strings
# Since the file is loaded in order we can create a dictionary object to remove duplicates
# Since the last entry is the one to keep overwritting keys will do what we need

newData={}
for line in taxRatesData:
    # Split string into list
    data=line.split(",")
    # Make first element the key and place the list as the value
    newData[data[0]]=data

# Create the list of lists which is now unique
output=list(newData.values())
map(str,output)
print(output)

# Write data to file
taxRatesOut = open("taxrates.csv","w")
taxRatesOut.write(header)
for line in output:
    taxRatesOut.write(",".join(line))
taxRatesOut.close()