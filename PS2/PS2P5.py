print ("Insert item name")
item = str(input())
print ("Insert item price")
price = float(input())
print ("Insert item discount")
discount = float(input())
print ("The discounted price of " + item + " is $" + str(price - (price * discount)))
                                                