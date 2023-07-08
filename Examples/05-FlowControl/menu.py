#!/usr/bin/env python

money=10.00

print("1 .. Current Balance")
print("2 .. Withdraw Cash")
print("3 .. Order a statement")
print("4 .. Return card")
choice=int(input('Enter choice> '))
if choice == 1:
	print("Balance is ",str(money))
elif choice == 2:
	amount=float(input('Enter amount to withdraw: '))
	print("Your balance is now: "+str(money-amount))
elif choice == 3:
	print("Statement has been sent")
elif choice == 4:
	print("Please remove card from slot")
else:
	print("Invalid option")
