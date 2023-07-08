#!/usr/bin/env python

phones = { 'steve': '555-4444', 'dave': '555-1111'}

for name in phones:
    print (name+"'s telephone number is "+phones[name])


for name, number in phones.items():
    print (name+"'s telephone number is "+number)
