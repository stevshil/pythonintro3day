#!/usr/bin/env python

import pandas as pd

df = pd.read_csv("powerusage.csv") #,index_col="StartDate")

# Print first 5 rows
print(df.head(5))

# Count number of items in each column
print(df.count())

# Show column data types
print(df.dtypes)

# Change the start date to datetime type
df["StartDate"] = pd.to_datetime(df["StartDate"])
print(df.dtypes)

# Select where date is greater than
print(df[df["StartDate"] >"2020-01-01"])

print("Data between 2016 and 2017")
print(df[df["StartDate"].between("2016","2017") ])