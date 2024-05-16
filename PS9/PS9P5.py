def cred_total (credit_hrs, code):
  if code == "I":
    total= 250*credit_hrs
  elif code == "O":
    total= 550*credit_hrs
  return(total)




loop=input("If you would like to begin enter,Yes: ")
while loop=="Yes":
  name=str(input("Enter student last name: "))
  credit_hrs=float(input("Enter amount of credit hours"))
  code=str(input("Enter district code: "))
  total_cred = cred_total(credit_hrs,code)

  print(name," the total tuition owed is $",total_cred)

  loop=input("If you would like to continue enter, Yes: ")


