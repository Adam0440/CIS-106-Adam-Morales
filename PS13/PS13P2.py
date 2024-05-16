class Students:
  def __init__(self,first,last,dc,credits):
    self.first=first
    self.last=last
    self.dc=dc
    self.credits=credits

  def tuition(self):
    if self.dc=="I":
      owed=self.credits*250
    else:
      owed=self.credits*500
    return (owed)

student1=Students("Adam","Morales","I",9)
student2=Students("Henry","Lopez","O",12)

print(student1.first,student1.last,student1.dc,student1.tuition())