print("insert make")
make=str(input())
print("insert model")
model=str(input())
print("insert msrp")
msrp=float(input())
print("insert discount")
discount=float(input())
print(f"The msrp is {msrp}. The discount is {discount}%. The discounted price of the {make}  {model} is ${msrp - (msrp * discount)}")
