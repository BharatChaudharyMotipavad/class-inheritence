# class in python
class Person:
  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname

  def name(self):
    print(self.fname,self.lname)

class Student(Person):
  def __init__(self,fname,lname):
    Person.__init__(self,fname,lname)

x = Student("Bharat","Chaudhary")
x.name()