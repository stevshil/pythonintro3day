#!/usr/bin/env python

import pandas as pd
import numpy as np

# Numpy array
array = np.array([[1, 1, 1], [2, 4, 8], [3, 9, 27], 
                  [4, 16, 64], [5, 25, 125], [6, 36, 216], 
                  [7, 49, 343]])

# creating a list of index names
index_values = ['first', 'second', 'third',
                'fourth', 'fifth', 'sixth', 'seventh']

# creating a list of column names
column_values = ['number', 'squares', 'cubes']

# creating the dataframe
df = pd.DataFrame(data = array, 
                  index = index_values, 
                  columns = column_values)

# Show the dataframe
print(df)

# Numpy array where first element will be the index
array = np.array([[1,1, 1, 1], [2,2, 4, 8], [3,3, 9, 27], 
                  [4,4, 16, 64], [5,5, 25, 125], [6,6, 36, 216], 
                  [7,7, 49, 343]])

# Change the columns
column_values = ['index','number', 'squares', 'cubes']
# Because NumPy arrays only take numbers we can't do as we would above
df2 = pd.DataFrame(data = array, 
                  columns = column_values)
# Set the first column as the index
df2=df2.set_index("index")
# Note how the column header is lower, denoting the index
print(df2)