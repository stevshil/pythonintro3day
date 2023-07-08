#!/usr/bin/env python

import sys

try:
	while True:
		print("You can only stop me with a control key")
		userinput=input("You can enter something here: ")
except KeyboardInterrupt:
	print("\nThank you I was getting dizzy")

print("End of program")
