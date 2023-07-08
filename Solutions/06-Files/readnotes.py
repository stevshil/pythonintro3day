#!/usr/bin/env python
from os.path import exists

# Check file exists
if not exists("mynotes.txt"):
    # Print message and exit as it does not
    print("The file mynotes.txt does not exist")
    exit()

# Open the file for read
notesData = open("mynotes.txt","r")
# Read in all the lines to our list
notesList = notesData.readlines()
# Close the file
notesData.close()

# Show the list with numbers
for idx,line in enumerate(notesList):
    print(str(idx)+": "+line.strip())

lineNumber=int(input("Enter the line number you wish to insert after: "))
# Add 1 to the line number chosen
lineNumber=lineNumber+1
# Get the note
data=input("Enter note: ")
if lineNumber == len(notesList):
    notesList.append(data)
else:
    notesList.insert(lineNumber,data+"\n")

# Write the data back to the file
notesData=open("mynotes.txt","w")
# Note we don't add the \n this time since it is already in the data from the read
notesData.writelines(notesList)
notesData.close()