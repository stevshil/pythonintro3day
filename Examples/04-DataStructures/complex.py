#!/usr/bin/env python

employees = { 
    'Steve': { 'EmpID': 1,
                'Role': 'Trainer',
                'Dept': 'IT',
                'Hobbies': ['Squash', 'Tennis', 'Motorcycling']},
    'Mike':  { 'EmpID': 2,
                'Role': 'Manager',
                'Dept': 'HR',
                'Hobbies': ['Shouting', 'Public Speaking']}
}

print("Steve's role is "+employees['Steve']['Role'])