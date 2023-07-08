#!/usr/bin/env python

myglobal="The Earth"

def tempfunc():
	global myglobal
	print("Inner: "+myglobal)	# global not required if printing
	myglobal="Planet Earth"
	print("Inner2: "+myglobal)
print("Outer: "+myglobal)
tempfunc()
print("Outer2: "+myglobal)
