#!/usr/bin/env python

rateOfVAT = 20
purchasePrice = int(input("Enter the purchase price: "))
exVATPrice = round(purchasePrice / (1 + (rateOfVAT/100)),2)
amountVAT = round(purchasePrice - exVATPrice,2)

print("The price excluding VAT is "+str(exVATPrice))
print("The amount of VAT is "+str(amountVAT))