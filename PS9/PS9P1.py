def calculate_total(price, quantity):
  total=quantity*price

  if total > 10000: 
   total = total -(total*0.10)

  return (total)

eprice=0
loop = input("Do you want to start? Yes or No: ")
while loop == "Yes":
  quantity = int(input("Enter quantity: "))
  price = float(input("Enter price: "))
  totalcost=calculate_total(quantity,price)
  print("Total Quantity: ",quantity, "Price per unit $","{:.2f}".format(price),"Total cost $","{:.2f}".format(totalcost))
  eprice=eprice+totalcost
  loop= input("Do you want to continue? Yes or No: ")
print("Total of all entries is", "{:.2f}".format(eprice))