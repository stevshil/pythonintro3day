#!/usr/bin/env python

# Documentation for the following package - https://docs.python.org/3/library/getpass.html
from getpass import getpass

# You will see the characters you type in at this prompt
username=input("Username: ")
# Note you will not see any characters printed on command line
password=getpass("Password: ")

print("You are:",username,"and your password is",password)