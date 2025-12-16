from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year
    def account_age(self):
        return 2025 - self.account_year
    @abstractmethod
    def get_role(self):
        pass
class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"Admin User: {self.name}"
class Guest(User):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return f"Guest User: {self.name}"
admin1 = Admin("Amrithesh", 2020)
guest1 = Guest("Rahul", 2023)
print(admin1.get_role())
print("Account Age:", admin1.account_age())
print(admin1)
print()
print(guest1.get_role())
print("Account Age:", guest1.account_age())
print(guest1)
