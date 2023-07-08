#!/usr/bin/env python

# Check numbers entered

intNumbers=[]
while ( len(intNumbers) < 6 ):
    entered=int(input("Enter number between 1 and 8: "))
    if entered > 0 and entered < 9:
        intNumbers.append(entered)

print(intNumbers)