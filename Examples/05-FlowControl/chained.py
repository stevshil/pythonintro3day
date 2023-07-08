#!/usr/bin/env python

number=int(input('Think of a number between 1 and 10: '))

if number >= 1 and number <= 10 :
	print("Then number you thought of was ", str(number))
else:
	print("Can't compute. I am broken: ",str(number))

# Can be written as
if 1 <= number <= 10 :
	print("Then number you thought of was ", str(number))
else:
	print("Can't compute. I am broken: ",str(number))
