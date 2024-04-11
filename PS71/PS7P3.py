
studentnmbr = 0
control = str(input("If you would like to start put Yes:"))
while control == "Yes":
  name = str(input("Enter student name: "))
  exam1 = float(input("Enter exam 1 score: "))
  exam2 = float(input("Enter exam 2 score: "))
  avg = (exam1 + exam2) / 2
  print (name, "has an average of", avg)
  studentnmbr = studentnmbr + 1
  control = str(input("If you would like to continue enter Yes: "))
print("Total number of students who participated, ", studentnmbr)