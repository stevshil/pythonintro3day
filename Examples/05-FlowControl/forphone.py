#!/usr/bin/env python

names=[]
numbers=[]
again='y'
while again != 'n':
    names.append(input("Enter name: "))
    numbers.append(input("Enter phone number: "))
    again=input("Another number to enter (y/n): ")

for idx, name in enumerate(names):
    print(name+" "+numbers[idx])