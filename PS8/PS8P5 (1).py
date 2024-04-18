f = open("PS8P5file.txt","r")
name = f.readline().rstrip('\n')
totaltuition=0
count=0
while name != "":
  dcode=str(f.readline().rstrip('\n'))
  costpercredit= 250 if dcode=="I" else 500
  credits=int(f.readline())
  tuition=credits*costpercredit
  print(name," credits taken: ",credits," total tuition: ",tuition)
  count=count+1
  totaltuition=totaltuition+tuition
  name=f.readline().rstrip('\n')

print("Total tuition,", totaltuition, "number of students: ",count)
