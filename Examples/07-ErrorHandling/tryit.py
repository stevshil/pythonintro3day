#!/usr/bin/env python

import sys
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))

try:
	result=number1/number2
except ZeroDivisionError:
	print("Please don't do that. Second numbers can't be zero")
	sys.exit(1)
print("result is:",str(result))
