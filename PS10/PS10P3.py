def discount(quantity,price,discrate):
  total=quantity*price
  discprice=price-(price*discrate)
  discamount=total-(discprice*quantity)
  return (discamount,discprice)

loop = input("Do you want to start? Enter Yes or No: ")
while loop =="yes":
  quantity=int(input("Enter the quantity: "))
  price=float(input("Enter the price: "))
  rate=float(input("Enter the discount rate in decimal: "))
  amountoff, newprice = discount(quantity,price,rate)

  print("The new price after discount is $,""  {:.2F}".format(newprice), "The amount saved is $","  {:.2F}".format(amountoff))
  loop=input("Do you want to continue? Enter Yes or No: ")