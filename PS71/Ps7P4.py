control = str(input"If you would like to continue put Yes.")
Totalpay=0
numberofemp=0

while control == "Yes":
  name = str(input("Enter employee name: "))
  hours = float(input("Enter hours worked: "))
  payrate = float(input("Enter pay rate: "))
  if hours<=40:
   pay=hours*payrate
  else:
   pay=40 * payrate + (hours - 40) *1.5 * payrate
  print("The weekly pay for",name,"is $",pay)
  Totalpay=Totalpay+pay
  numberofemp = numberofemp + 1
  control= str(input("If you would like to continue put Yes."))

print("The total pay for all employees is $",Totalpay)
averagepay=Totalpay/numberofemp
print("The average pay for all employees is $",averagepay)

