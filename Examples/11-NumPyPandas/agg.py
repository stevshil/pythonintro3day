#!/usr/bin/env python

import numpy as np
npa = np.arange(15).reshape(3,5)
print(repr(npa))

# Entire array
print("Sum of array: "+repr(npa.sum()))
print("Sum of array: "+repr(npa.min()))
print("Sum of array: "+repr(npa.max()))
print("Sum of array: "+repr(npa.mean()))

# Down the columns [col1, col2, ....]
print("Sum of array: "+repr(npa.sum(axis=0)))

# Across the rows [row1, row2, ...]
print("Sum of array: "+repr(npa.sum(axis=1)))