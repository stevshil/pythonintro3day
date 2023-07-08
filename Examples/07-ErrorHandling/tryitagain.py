#!/usr/bin/env python

import sys
try:
	number1=int(input("Enter first number: "))
	number2=int(input("Enter second number: "))
	result=number1/number2
except ZeroDivisionError:
	print("Please don't do that. Second numbers can't be zero")
	sys.exit(1)
except ValueError:
	print("That. Was not a number!")
	sys.exit(2)
except KeyboardInterrupt:
	print("OK I'll exit, but you didn't need to be so rough")
	sys.exit(2)
print("result is:",str(result))
