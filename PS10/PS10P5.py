def calc_total(quantity,price):
  global total 
  global tax 
  total=quantity*price
  tax=total*0.7
  total+=tax
  return()

loop = input("Do you want to start? Yes or No: ")
while loop == "Yes":
  quantity=int(input("Enter the quantity: "))
  price=float(input("Enter the price: "))

  calc_total(quantity,price)

  print("The total price is $", "{:.2F}".format(total), "The tax amount is $", "{:.2F}".format(tax))
  loop = input("Do you want to run the program again? Yes or No: ")