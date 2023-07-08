#!/usr/bin/env python

words=['animal','vegetable','mamal','goose','gander']
counter=0

for word in (words):
    if 'e' not in word:
        continue
    else:
        counter+=1
        print(word,"contains e")

print("There are",counter,"words with e")
