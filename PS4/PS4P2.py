purchase = float(input("Enter the amount of the initial purchase: "))
current = float(input("Enter the current stock price: "))
quantity = float(input("Enter quantity of stock: "))

newvalue = (current-purchase)*quantity

print("The stock has shifted to ",newvalue )
