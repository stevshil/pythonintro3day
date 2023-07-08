#!/usr/bin/env python

# Single element
intNumbers = [ 10, 20, 35, 42, 56 ]
# Remember lists start from 0
print(intNumbers[2]) # 35

# Elements 1 to 3
intNumbers = [ 10, 20, 35, 42, 56 ]
print(intNumbers[1:3]) # [ 20, 35 ]
# Note you don't see element 3 as it is the END
# Therefore slice END is not inclusive index

intNumbers = [ 10, 20, 35, 42, 56, 74, 82, 88, 99 ]
print(intNumbers[:3]) # [ 20, 35 ]
print(intNumbers[5:])
print(intNumbers[::2])
print(intNumbers[::3])
print(intNumbers[1::3])