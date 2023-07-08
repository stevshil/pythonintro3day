#!/usr/bin/env python

phoneBook = { 'Steve' : '555-1234', 
              'Mike': '555-9999', 
              'George': '555-4398' }
print(phoneBook)
print(phoneBook['Mike'])
print(phoneBook.keys())
print(phoneBook.values())
del phoneBook['Mike']
print(phoneBook.keys())
phoneBook['Steve']=None
print(phoneBook)


employees = {}
employees['Steve'] = 'Trainer'
print(employees)