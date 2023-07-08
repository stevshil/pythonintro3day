#!/usr/bin/env python

permissions='rw-'

if 'r' in permissions:
	print("Is readable")

if 'w' in permissions:
	print("Is writable")

if 'x' in permissions:
	print("Is executable")


login = [ ['steve', 'letmein'],
	[ 'dave', 'letmeout'],
	[ 'george', 'whereami'],
	[ 'bill', 'heretohelp' ]
]

username=input('Username: ')
passwd=input('Password: ')

if [ username, passwd ] in login:
	print("Welcome ", username)
else:
	print("Access not granted!")
