name=str(input("Enter last name: "))
Dependants=float(input("Enter number of dependants: "))
gross=float(input("Enter gross income: "))

adjusted = gross - (Dependants * 1200)

tax= 0.2 if adjusted > 50000 else 0.1

incometax= adjusted * tax

if incometax < 0: 
  incometax=100
else:
  None
print("Last name is, ", name,"The number of dependants is, ",Dependants,f"The gross income is, ${gross:.2f}",f"The adjusted income is, ${adjusted:.2f} ",f"The income tax will be ${incometax:.2f}")