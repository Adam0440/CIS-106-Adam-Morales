qty=float(input("Enter the quantity of the item: "))
if qty >= 1000:
  unitprice = 3.00
else:
  unitprice = 5.00  
extprice = qty * unitprice
tax = extprice*0.07
total = extprice + tax
print("The quantity is, ",qty, "The unit price is, ",unitprice, f"The extended price is,{extprice:.2f}",f" The tax is,{tax:.2f}",f"The total is,{total:.2f}")