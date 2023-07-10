#!/usr/bin/env python

import pandas as pd

# Basic import setting no index, note numerical index column generated
df = pd.read_csv("dormantcos.csv")
print("DataFrame subset of rows")
print(df)

# Setting the index
df = pd.read_csv("dormantcos.csv", index_col="Company Number")

print("Showing the first 2 rows from the top of the DataFrame")
print(df.head(2))
# Use tail() for last rows

print("Show the index and the Company Name column")
print(df["Company Name"])
# Note only the Index column name shows

print("Show Company Name and Number of Shares columns")
print(df[["Company Name","Number Shares"]])
# Note how the column names show this time

print("Show index detail")
print(df.index)

print("Transpose the dataframe")
print(df.T)

print("Show a specific row given the index value")
print(df.loc["ec094061FeaF7Bc"])

print("Show row based on row numbers like an list, so start at 0")
print(df.iloc[0])
# This means you can use DataFrame like a list, so splicing, etc

print("Mean: "+repr(df["Share Price"].mean()))
print("Max: "+repr(df["Share Price"].max()))
print("Sum: "+repr(df["Share Price"].sum()))

print(df.agg({"Share Price":["sum","mean"],"Number Shares":["sum","mean"]}))