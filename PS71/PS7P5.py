totaldisc = 0
control = str(input("If you would like to start put Yes:"))
while control == "Yes":
  qty = float(input("Enter quantity: "))
  price = float(input("Enter price: "))
  ext = qty * price
  if ext > 10000:
    discount = ext * 0.25
  else: 
    discount = ext * 0.10
  total = ext - discount
  print("The extended price is,",ext,"The discount is,", discount, "The total is,", total)
  totaldisc = totaldisc+discount
  control = str(input("If you would like to continue enter Yes: "))
print("The sum of all the discounts is,",totaldisc)