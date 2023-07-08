#!/usr/bin/env python

import json
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
jsonEmployees = json.dumps(employees)
print(jsonEmployees)
