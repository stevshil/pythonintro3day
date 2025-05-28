import os
import sys

if sys.argv[1] == "DEBUG":
    print("Startingi in DEBUG mode")

longoutput = False
alloutput = False
otherargs = []

# Iterate through arguments
for arg in sys.argv[1:]:
    if arg == "l":
        longoutput = True
    if arg == "a":
        alloutput = True
    if arg not in ("l", "a", "DEBUG"):
        otherargs.append(arg)

if len(otherargs) > 0:
    for dirname in otherargs:
        try:
            for filename in os.listdir(dirname):
                print(dirname+"/"+filename)
                if longoutput:
                    filepath = os.path.join(dirname, filename)
                    try:
                        stat = os.stat(filepath)
                        print(f"  Size: {stat.st_size} bytes, Modified: {stat.st_mtime}")
                    except Exception as e:
                        print(f"  Error getting attributes: {e}")
                if not alloutput and filename.startswith('.'):
                    continue
        except Exception as e:
            print(f"Error accessing directory {dirname}: {e}")
else:
    for filename in os.listdir('.'):
        print(filename)