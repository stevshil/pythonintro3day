#!/usr/bin/env python

import numpy as np

# Basic object, single dimension array of 15 elements
npa = np.arange(15)
print(repr(npa))

# Change the shape to 3 rows of 5 columns
npb=npa.reshape(3,5)
print(repr(npb))

# Tell me the shape
print("npb has the following (rows, columns): "+repr(npb.shape))

# Number of dimensions
print("npb has the following number of dimensions: "+repr(npb.ndim))

# Number of elements
print("npb has "+repr(npb.size)+" elements")

# You can also create NumPy arrays from a list
npc = np.array([1,2,3,4])
print(repr(npc))