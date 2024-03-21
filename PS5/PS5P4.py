Name=str(input("Enter name of appliance, "))
price=float(input("Enter price of appliance, "))
if price > 1000: warranty = price*0.10
else:
  warranty = price*0.05
total = price + warranty
print("Name of appliance is, ", Name, f"The price of appliance is, ${price:.2f}",f"The warranty will be ${warranty:.2f} " f"The total cost will be, ${total:.2f}.")