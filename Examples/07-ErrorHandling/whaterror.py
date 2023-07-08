#!/usr/bin/env python

try:
	number1=int(input("Enter a number: "))
	number2=int(input("Enter a number: "))
	result=number1/number2
except (ValueError, ZeroDivisionError) as err:
	print("There was some problem")
	print(err)
else:
	print(str(result))