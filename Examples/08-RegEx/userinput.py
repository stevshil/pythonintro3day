#!/usr/bin/env python

import re

answer='y'
while re.search('^[yY]',answer):
	print("around we go again")
	answer=input("Again (y/n)? ")

print("End of program")
