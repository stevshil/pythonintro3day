#!/usr/bin/env python

# Enter 10 numbers
intNumbers=[]
intNumbers.append(int(input("Enter number between 1 and 8: ")))
intNumbers.append(int(input("Enter number between 1 and 8: ")))
intNumbers.append(int(input("Enter number between 1 and 8: ")))
intNumbers.append(int(input("Enter number between 1 and 8: ")))
intNumbers.append(int(input("Enter number between 1 and 8: ")))
intNumbers.append(int(input("Enter number between 1 and 8: ")))

# Check that the list has 10 numbers
print("The list contains: "+str(len(intNumbers)))

# How many times does the number 5 appear in the list
print("The user has entered "+str(intNumbers.count(5))+" number 5s")

# Last 3 elements
print("Last 3 numbers: "+str(intNumbers[-3:]))

# Every 3rd element from index 1
print("Every 3rd element from index 1: "+str(intNumbers[1::3]))

# Sort the list in reverse
intNumbers.sort(reverse=True)
print("Reversed sorted list: "+str(intNumbers))