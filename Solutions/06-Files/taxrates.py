#!/usr/bin/env python

from os.path import exists

again='y'
employees={}

while again == 'y':
    fullname=input("Please enter employee name: ")
    empid=input("Please enter employee ID: ")
    salary=float(input("Please enter employee salary: "))
    again=input("Do you wish to enter another employee (y/n): ")

    # Add data to dictionary
    employees[empid] = {'name': fullname, 'salary': salary}

# print(employees)

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

# Write employees to file
datafileExists=0

if not exists("taxrates.csv"):
    datafileExists=1

header="ID,Name,Salary,Basic,Higher,Additional"
taxratesOut=open("taxrates.csv","a")
if datafileExists == 1:
    taxratesOut.write(header+"\n")

for employee in employees:
    # Employee is the employee ID
    print(employees[employee])
    if "basic" in employees[employee]:
        basic=employees[employee]['basic']
    else:
        basic=0.00
    if "higher" in employees[employee]:
        higher = employees[employee]['higher']
    else:
        higher=0.00
    if "additional" in employees[employee]:
        additional=employees[employee]['additional']
    else:
        additional=0.00

    data=employee+","+employees[employee]['name']+","+str(employees[employee]['salary'])+","+str(basic)+","+str(higher)+","+str(additional)
    taxratesOut.write(data+"\n")
