def mpg(miles, gallons):
    mpg = miles/gallons
    return mpg
totaltrips=0

loop=input("If you wouls like to start, enter Yes: ")
while loop == "Yes":
    destination=input("Enter your destination city: ")
    gallons=float(input("Enter the amount of gallons used: "))
    miles=float(input("Enter the amount of miles driven: "))
    mpg=mpg (miles,gallons)
    print("The city you drove to was,",destination,"The amount of miles driven was,",miles,"The amount of gallons used was,",gallons,"The miles per gallon was,",mpg)
    totaltrips=totaltrips+1
    loop=input("If you would like to continue, enter Yes: ")

print("The total amount of trips is,",totaltrips )
