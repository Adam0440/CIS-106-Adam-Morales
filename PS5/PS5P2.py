item=str(input("Enter the name of the item: "))
qty=float(input("Enter the quantity of the item:"))
if item== "A":
  unitprice=10.00
else:
  unitprice=20.00
extprice=qty*unitprice
print("The item is, ",item, "The quantity is, ",qty, "The unit price is, ",unitprice,"The extended price is, ",extprice)