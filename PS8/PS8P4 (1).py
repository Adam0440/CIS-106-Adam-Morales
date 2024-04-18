from typing import Counter


f = open("PS8P4file.txt","r")
item = f.readline().rstrip('\n')
totalextp=0
count=0
while item != "":
  qty = int(f.readline())
  price = int(f.readline())
  extprice = qty * price
  print("Item name is",item,"The quantity is, ",qty,"The price is, ",price,"Extended price is, ",extprice)
  count=count+1
  totalextp=totalextp+extprice
  item=f.readline().rstrip('\n')


avg=totalextp/count
print("The total amount of extended price is,", totalextp,"The amount of orders is,",count,"The average order is, ",avg)
  