def grade_total(test1,test2,test3):
  global total
  global average
  total=test1+test2+test3
  average=total/3
  return()

test1=float(input("Enter the score for test 1: "))
test2=float(input("Enter the score for test 2: "))
test3=float(input("Enter the score for test 3: "))

grade_total(test1,test2,test3)


print("The total amount of points is", total, "The average score is","{:.2F}".format(average))