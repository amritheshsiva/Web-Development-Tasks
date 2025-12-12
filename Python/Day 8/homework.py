class Employee :
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def display(self):
        print("Employee's name:",self.name)
        print("Employee's role:", self.role)
class Trainer(Employee):
    def __init__(self,name,role,specialization):
        Employee.__init__(self,name,role)
        self.specialization =specialization 
    def display(self):
        print("Name :",self.name)
        print("Role :",self.role)
        print("Specialization :",self.specialization)
class YogaInstructor(Employee):
    def __init__(self,name,role,yoga_style):
        Employee.__init__(self,name,role)
        self.style=yoga_style
    def display(self):
        print("Name :",self.name)
        print("Role :",self.role)
        print("Style :",self.style)
class MultiTrainer(Trainer,YogaInstructor):
    def __init__(self,name,role,specialization,yoga_style):
        Trainer.__init__(self,name,role,specialization)
        YogaInstructor.__init__(self,name,role,yoga_style)
    def display(self):
        print("Name :",self.name)
        print("Role :",self.role)
        print("Specialization :",self.specialization)
        print("Style :",self.style)


emp=Employee("Arjun","Staff")
trainer=Trainer("Jishnu","Trainer","Strength")
yoga=YogaInstructor("Hemand","Yoga Instructor","Normal")
multi=MultiTrainer("Vaibhav","Multi-Trainer","HIIT","Normal")

emp.display()
trainer.display()
yoga.display()
multi.display()