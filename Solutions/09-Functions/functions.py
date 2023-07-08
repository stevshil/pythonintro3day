#!/usr/bin/env python

# Basic Lab part 1
def again():
    answer=input("Do you wish to try again (y/n)? ")
    if answer == 'y' or answer == 'Y':
        return True
    else:
        return False
    
while again():
    print("Running the script again")

print("End of program, goodbye")

# Basic Lab part 2
def sum(numList):
    foundString=0
    for num in numList:
        try:
            print("String found "+num)
            foundString=1
            return False
        except:
            # If here then it is a number so OK
            continue
        
    if foundString == 0:
        result=0
        for num in numList:
            result=result+num
        print(result)
        return result
    

numbers=[2,3,4,5]
mixed=[2,"hello",3,4,5]
sum(numbers)
sum(mixed)