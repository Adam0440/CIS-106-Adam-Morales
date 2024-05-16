def grosspay (code, hours):
 if hours<= 40:
  payrate = hours * code
 else:
   payrate = 40 * code + (hours - 40) *1.5 * code
 return payrate

totalpay=0

loop = input("If you would like to start, enter Yes: ")
while loop == "Yes":
  name = str(input("Enter employee name: "))
  hours = float(input("Enter hours worked: "))
  code= str(input("Enter pay code: "))
  if code == "L":
            code =25
  elif code == "A":
            code =30
  elif code == "J" :
      code = 50
  weekly_pay = grosspay (code, hours)
  totalpay= weekly_pay + totalpay
  print("The weekly pay for",name,"is $",weekly_pay)

  loop= input("If you would like to continue, enter Yes: ")

print("The total pay for all employees is $",totalpay)



