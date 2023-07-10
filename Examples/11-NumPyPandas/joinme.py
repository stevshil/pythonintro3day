#!/usr/bin/env python

import pandas as pd

df1 = pd.DataFrame.from_dict([
    {"Name": "John", "Age": 40},
    {"Name": "Bob", "Age": 20},
    {"Name": "George", "Age": 54}
])

df2 = pd.DataFrame.from_dict([
    {"Name": "David", "Age": 58},
    {"Name": "Steve", "Age": 32}
])

# Use ignore_index=True to generate new index values, rather than duplicate
allData = pd.concat([df1,df2], ignore_index=True)
print(allData)

hobbies = pd.DataFrame.from_dict([
    {"Name": "George", "Hobbies": ["Golf","Whisky","Friends"]},
    {"Name": "Steve", "Hobbies": ["Motorbikes","Tennis","Computers"]}
])

# Join without index
print(allData.join(hobbies["Hobbies"], how="inner"))
# Note how it takes first rows from each DF

# Setting index and column to join on
newData=allData.join(hobbies.set_index("Name"), how="inner", on="Name")
print(newData)
# Now our data for hobbies matches owner

# Show all from the allData DF
print(allData.join(hobbies.set_index("Name"), how="left", on="Name"))