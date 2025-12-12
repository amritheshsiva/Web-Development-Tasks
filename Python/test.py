class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def intro(self):
    print("Hello my name is " + self.name)

stud1 = Student("Kevin", 26)
stud1.intro()