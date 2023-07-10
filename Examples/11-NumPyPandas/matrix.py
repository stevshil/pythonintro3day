#!/usr/bin/env python

import numpy as np

m1 = np.array([[1,1],
               [0,1]])

m2 = np.array([[2,0],
               [3,4]])

# Multiple corresponding elements
print(repr(m1*m2)) # That's 2x1, 1x0 and 3x0 and 4x1
# Vectorizing
print(repr(m1+m2)) # Addition or Vectorizing
# Product
print(repr(m1@m2))
# or
print(repr(m1.dot(m2)))