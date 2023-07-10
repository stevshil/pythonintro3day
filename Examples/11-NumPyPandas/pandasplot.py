#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("powerusage.csv",index_col="StartDate")
df.drop(columns=["day_of_week","notes"],inplace=True)
df.rename(columns={"Value (kWh)":"kwh"},inplace=True)
df["kWh2"]=df["kwh"].cumsum(axis=0)
print(df.head())
df.plot() # Basic chart
df.plot(kind="scatter", x="kwh", y="kWh2")
plt.show()