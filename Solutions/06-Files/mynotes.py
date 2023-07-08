#!/usr/bin/env python

notesData=open("mynotes.txt","a")

mynote=None

while mynote != "exit":
    mynote = input("Enter note: ")
    if mynote != "exit":
        notesData.write(mynote+"\n")

notesData.close()