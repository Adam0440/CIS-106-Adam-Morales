books=float(input("Enter the number of books: "))
price=float(input("Enter the price per book: "))
total=books*price
if total>50: 
  shipping=0
  else shipping=25
print("The order total is, ",total,"The shipping charge is, ",shipping,"The total order is, " total+shipping)