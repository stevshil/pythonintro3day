#!/usr/bin/env python

import sys

try:
	number1=int(input("Enter first number: "))
	number2=int(input("Enter second number: "))
	result=number1/number2
except:
	print("Please don't do that. Numbers can't be zero, empty or strings")
	sys.exit(1)

print("result is:",str(result))
