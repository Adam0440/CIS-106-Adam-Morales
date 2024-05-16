from myfunctions12 import sales_forecast

control=str(input("Enter Yes if you would like to start: "))
while control.lower() == "yes":
  name=input("Enter the salesperson's name: ")
  month=input("Enter the month in 3 letter form: ")
  month=month.lower()
  sales=float(input("Enter the sales made: "))
  forecasted_sales=sales_forecast(month, sales)
  print("Salesperson ",name," Will sell ","{:.2F}".format(forecasted_sales),"Next Month")
  control=str(input("Enter Yes if you would like to continue: "))
forecast=0