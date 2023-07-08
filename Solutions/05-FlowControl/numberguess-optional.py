#!/usr/bin/env python

from random import random
randnum = int(random()*10)+1

guess=0
guessed=0
for guesses in range(3):
    while guess < 1 or guess > 10:
        guess = int(input("Please enter a number between 1 and 10: "))

    if guess == randnum:
        print("You have guessed correctly the number "+str(randnum))
        guessed=1
        break
    else:
        print("That is not correct")
    guess=0

if guessed == 0:
    print("You did not guess the number, which was "+str(randnum))