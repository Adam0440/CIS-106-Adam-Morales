from myfunctions12 import square_footage 

loop = input("Do you want to start? Enter Yes or No: ")
while loop == "Yes":
  height = input(float("Enter the height of the room: "))
  width = input(float("Enter the width of the room: "))
  length = input(float("Enter the length of the room: "))
  square_footage = square_footage(length, width, height)
  totalgallons= square_footage/50
  print("The total # of gallons needed will be ",totalgallons)
  loop = input("Do you want to go again? Enter Yes or No: ")