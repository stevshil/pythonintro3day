#!/usr/bin/env python

import sys
operator=sys.argv[1]
num1=sys.argv[2]
num2=sys.argv[3]

answer=eval(num1+operator+num2)
print(num1+operator+num2+" = "+str(answer))