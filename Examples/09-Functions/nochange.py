#!/usr/bin/env python

def changeMeNot(strName):
	print("Passed value: "+strName)
	strName="Arthur Crown"
	print("In function change "+strName)

mainName="Steve Shilling"
print("Before call "+mainName)
changeMeNot(mainName)
print("Name in main "+mainName)
