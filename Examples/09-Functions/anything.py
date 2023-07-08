#!/usr/bin/env python

def addnums(a,b):
	tmp=[ ]
	for perms in range(3):
		tmp.append(a+b*perms)
	return tmp

result = addnums(20,30)
print(result)
