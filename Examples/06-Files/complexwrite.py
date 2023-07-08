#!/usr/bin/env python

import pickle

# Our data structure
theData = {'steve': {'age': 36, 'gender': 'male'}, 'dave': {'age': 40,'gender':'male'}}
print(theData) # Show the format of the data

# Open the file to store the data
complexData = open("complexdata.dat", "wb")
# Write the data into a file in a Python format
pickle.dump(theData, complexData)
# Close the file
complexData.close()

rfh = open("complexdata.dat","rb")
dict2=pickle.load(rfh)
print(dict2)
rfh.close()
