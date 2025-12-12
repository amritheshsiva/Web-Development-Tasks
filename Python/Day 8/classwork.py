class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def  show_details(self):
        print("The person's name is {} and age is {}".format(self.name,self.age))

class Employee(Person):
    def __init__(self,name,age,employee_id):
        Person.__init__(self, name, age)
        self.id=employee_id
    def show_details(self):
        print("Name : ",self.name)
        print("Age :",self.age)
        print("Employee ID :",self.id)
class PartTime(Person):
    def __init__(self,name,age,working_hours):
        Person.__init__(self, name, age)
        self.work=working_hours
    def show_details(self):
        print("Name : ",self.name)
        print("Age :",self.age)
        print("Working Hours :",self.work)
class Consultant (Employee,PartTime):
    def __init__(self,name,age,employee_id,working_hours,project_name):
        Employee.__init__(self, name, age, employee_id) 
        PartTime.__init__(self, name, age, working_hours)
        self.project=project_name
    def show_details(self):
        print("Name : ",self.name)
        print("Age :",self.age)
        print("Employee ID :",self.id)
        print("Working Hours :",self.work)
        print("Project Name",self.project)

person=Person("Arjun",22)
employee=Employee("Astle",25,"ID_15")
part_time=PartTime("Jishnu",22,2.0)
consultant=Consultant("Vasu",24,"ID_30",3.0,"Flutter")
person.show_details()
employee.show_details()
part_time.show_details()
consultant.show_details()
