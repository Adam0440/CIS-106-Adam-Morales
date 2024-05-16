def battin_avg(hits,bats):
    batavg=hits/bats
    return batavg




for count in range(1,10,1):
  name=input("Enter players name")
  hits=int(input("Enter number of hits"))
  bats=int(input("Enter number of times player batted"))
  batavg=battin_avg(hits,bats)
print("Total # of player",count)