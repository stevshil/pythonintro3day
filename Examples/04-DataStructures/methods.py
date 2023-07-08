#!/usr/bin/env python

strWords = ['tonight', 'tomorrow', 'to', 'another', 'day', 'to']
print(strWords.count('to'))
print(strWords.index('day'))
print(strWords.index('to'))
print(strWords.index('to',3))

strWords.reverse()
print(strWords)

strWords.pop(2)
print(strWords)
strWords.remove('to')
print(strWords)

strWords = ['tonight', 'tomorrow', "3", 'to', 'another', "10", 'day', 'to']
strWords.sort()
print(strWords)

strWords.sort(key=len)
print(strWords)