#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

dfStocks = pd.read_json("./sample-stocks-data.json")
print(dfStocks.head(5))
dfStocks.set_index("symbol",inplace=True)
print(dfStocks.head(5))
dfStocks.drop(columns=["description"],inplace=True)
print(dfStocks.head(5))
print(dfStocks.isna().sum().T)
print(dfStocks.agg({"initial_price": ["max"]}))
print(dfStocks[dfStocks["initial_price"] == dfStocks["initial_price"].max()])

fig, axes = plt.subplots(nrows=1, ncols=3)
dfStocks.plot(ax=axes[0])
axes[0].set_title("Basic")
dfStocks.plot(kind="bar", ax=axes[1])
axes[1].set_title("Bar")
dfStocks["initial_price"].plot(ax=axes[2], figsize=(15,8))
axes[2].set_title("Initial Price")
plt.show()

dfStocks.to_csv("stocks.csv")