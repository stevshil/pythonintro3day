#!/usr/bin/env python

def named(name="Default name",age=21,car="Nissan Micra"):
	myparameters=[name,age,car]
	print(myparameters)

named(name="Steve")
named(age=42)
named(name="Steve",car="Lotus Esprit")
