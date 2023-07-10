#!/usr/bin/env python

import pandas as pd

df = pd.read_csv("powerusage.csv",index_col="StartDate")

# Drop the notes column and store in new DF
newdf=df.drop(columns=["notes"])
print(newdf)
print(df)

# Drop the notes and day_of_week columns in the original DF
df.drop(columns=["notes","day_of_week"],inplace=True)
print(df)

# Rename column
df.rename(columns={"Value (kWh)":"kwh"},inplace=True)
print(df)

print("Count the number of Nulls in the data set")
print(df.isnull().sum())

print("Count number of not a number NaN")
print(df.isna().sum())

print("Count a specific column for NaN")
print(df["kwh"].isna().sum())

print("Fill NaN values in kwh with 0.5")
df["kwh"] = df["kwh"].fillna(0.5)

print("Mean of kwh column")
print(df["kwh"].mean())

print("Fill NaN values with mean of kwh")
df["kwh"] = df["kwh"].fillna(df["kwh"].mean())

# There are other methods you could use including .interpolate()