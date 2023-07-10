#!/usr/bin/env python

import numpy as np
import numpy.linalg as la

npa = np.arange(15).reshape(3,5)
print(repr(npa))

# Filtering
# Extract all elements that are divisible by 2
print(repr(npa[npa % 2 == 0]))
# Note the single dimension

# Arithmetic
print(repr(np.cos(npa)))

# Slicing still works
np1=np.arange(15)
print(repr(np1[0:4]))

# Linear algebra
print(repr(la.norm(npa)))
print(repr(la.svd(npa)))