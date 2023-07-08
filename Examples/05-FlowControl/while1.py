#!/usr/bin/env python

userinput='y'
while userinput == 'y':
  userinput=input('Again (y/n)? ')
  print('round we go again')

print("and now we're done")

x=1
sum=0
while x <= 10:
    print(x * 2)
    sum+=x
    x+=1

print("Total of x is: ",str(sum))
