#!/usr/bin/env python

def changeMe(listNames):
	print("Passed values: "+str(listNames))
	listNames[0]="Arthur"
	print("In function change "+str(listNames))

mainNames = ["Steve","Augie"]
print("Names in main "+str(mainNames))
changeMe(mainNames)
print("Names in main again "+str(mainNames))
