#!/usr/bin/env python

# Create a new file, or overwrite if exists
companyData = open("companies.txt", "w")

# Writing individual lines
name="Steve Shilling"
role="Technical Trainer"

companyData.write(name+"\n")  # Note the addition of newline
companyData.write(role+"\n")

# Dumping a list
todo = ["Raise invoice","Chase payment","Submit company accounts"]
companyData.writelines(todo)

# Dumping a list
todo = ["Raise invoice","Chase payment","Submit company accounts"]
companyData.writelines(map(lambda x: x+"\n",todo))

# Close the file, to confirm we are finished
companyData.close()