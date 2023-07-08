#!/usr/bin/env python

companyData = open("companies.txt", "r")

# Using a loop to read lines
for line in companyData:
    print(line.strip())

companyData.close()

# Open the file for reading
companyInfo = open("companies.txt","r")

# Read all the lines into the allData list
allData=companyInfo.readlines()
companyInfo.close()

# Prints the list to the screen including the brackets
print(allData)
