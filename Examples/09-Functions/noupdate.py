#!/usr/bin/env python

def changeme(mynames):
	mynames[0]="Is Earl"
	print("In function: "+repr(mynames)

thesenames=['Bob','Eric']
print("Before function: "+repr(thesenames))
changeme(thesenames[:])
print("After function: "+repr(thesenames))
