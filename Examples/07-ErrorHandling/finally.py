#!/usr/bin/env python

# Check to see if we can open the file
try:
	fh=open("Afile.txt","w")
except IOError as err:
	print("The file Afile.txt cannot be opened")
	print(err)
number=0
try:
	while True:
		# Use ^C to cause exception
		theline="The number is "+str(number)+"\n"
		fh.write(theline)
		number+=1
except(KeyboardInterrupt):
	print("Signal aborted program")
finally:
	print("Cleaning up.")
	fh.close()

print("Program ended")
