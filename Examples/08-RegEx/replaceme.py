#!/usr/bin/env python

import re

theText="This is the old with the new"
newText = re.sub('old', 'new', theText)
print(theText)
print(newText)

moreText="The snake eat the cat who eat the mouse"
newText = re.sub(' eat.*cat','', moreText)
print(moreText)
print(newText)
