#!/usr/bin/env python

again='y'
employees={}

while again == 'y':
    fullname=input("Please enter employee name: ")
    empid=input("Please enter employee ID: ")
    salary=float(input("Please enter employee salary: "))
    again=input("Do you wish to enter another employee (y/n): ")

    # Add data to dictionary
    employees[empid] = {'name': fullname, 'salary': salary}

print(employees)

for employee in employees.keys():
    basic=0
    higher=0
    additional=0
    salary = employees[employee]['salary']
    if salary > 125140:
        additional = float(salary - 125140)*.45
        higher = float(salary - 125140 - 50270) * .4
        basic = float(salary - 125140 - 50270 - 12570) * .2
    if salary >= 50271 and salary <= 125140:
        higher = float(salary - 50270)*.4
        basic = float(salary - 50270 - 12570) * .2
    if salary > 12570 and salary <= 50270:
        basic = float(salary - 12570) * .2
    
    employees[employee]['basic']=basic
    employees[employee]['higher']=higher
    employees[employee]['additional']=additional

print(employees)
