#!/usr/bin/env python
import pprint

todos={ "todos": [
    {
        "id": 1,
        "todo": "Do something nice for someone I care about",
        "completed": "true",
        "userId": 26
    },
    {
        "id": 2,
        "todo": "Memorize the fifty states and their capitals",
        "completed": "false",
        "userId": 48
    } ],
    "total": 150,
    "skip": 0,
    "limit": 2
}

# Print the total entries, 150 value
print("Total number of todos: "+repr(todos["total"]))

# Print the userId for the 2nd entry
print("User: "+str(todos["todos"][1]["userId"]))
# Should print 48

# Print the first entry todo description
print(todos["todos"][0]["todo"])

# Update the 2nd entry completed from false to true
todos["todos"][1]["completed"]="true"

# Display the entire dictionary
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(todos)