f = open("bonus.txt","r")
name=f.readline().rstrip('\n')
totalbonus=0
while name !="":
  salary = float(f.readline()) 
  print (name)
  if salary >= 100000:
      bonusrate=0.20
  elif salary >= 50000:
    bonusrate=0.15
  else:
    bonusrate=0.10
  bonus=salary*bonusrate
  print(name, "salary: ", salary, "bonus: ", bonus)
  totalbonus= totalbonus+bonus
  name = f.readline()
print("Total bonus: ", totalbonus)

