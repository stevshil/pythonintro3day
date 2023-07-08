#!/usr/bin/env python

login = [ ['steve', 'letmein'],
	[ 'dave', 'letmeout'],
	[ 'george', 'whereami'],
	[ 'bill', 'heretohelp' ]
]

try:
    username=input('Username: ')
    passwd=input('Password: ')
except:
	print("\nExiting the program as invalid key press")
	exit()

if [ username, passwd ] in login:
	print("Welcome ", username)
else:
	print("Access not granted!")
