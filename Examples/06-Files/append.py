#!/usr/bin/env python

# Create a new file if it does not exist, or add to the end
companyData = open("companies.txt", "a")
companyData.write("This line has been added\n")
companyData.close()
