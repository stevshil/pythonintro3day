#!/usr/bin/env python

# Get the grade and store as an integer
grade = input("Please enter your grade as a percentage: ")
grade = int(grade)

if grade >= 0 and grade <= 49:
    print("You have an F grade")
elif grade > 49 and grade <= 59:
    print("You have an E grade")
elif grade > 59 and grade <= 69:
    print("You have a D grade")
elif grade > 69 and grade <= 79:
    print("You have a C grade")
elif grade > 79 and grade <= 89:
    print("You have a B grade")
elif grade > 90 and grade <= 100:
    print("You have an A grade")
else:
    print("A valid grade between 0 and 100 is required.")

if grade == 100:
    print("You have a Distinction")