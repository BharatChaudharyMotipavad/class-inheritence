# class in class in python
class Person:
  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname
  
  def fullname(self):
    print(self.fname,self.lname)

class Student(Person):
  def __init__(self,fname,lname):
    Person.__init__(self,fname,lname)
  
p1 = Student("Bharat","Chaudhary")

p1.fullname()
