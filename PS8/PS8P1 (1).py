loop = (input("Y if you would like to loop"))
while loop == "Y":
  p = float(input("Enter principal amount: "))
  r = float(input("Enter interest rate: "))
  total_i=0
  print("\n Year", "Beginning Balance", "Ending Balnce")
  for y in range (1,6,1):
    i = p * r
    eb = i + p
    print ("\n Year", y, "{:.2f}" .format(p), "{:.2f}" .format(eb))
    p = eb
    total_i = total_i + i
  print("\n Total interest earned: ", "{:.2f}" .format(total_i))
  loop = (input("Y if you would like to loop"))
    