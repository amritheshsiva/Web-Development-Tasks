class Account:
    def __init__(self, name, balance):
        self._name = name        
        self._balance = balance 
    def calculate_interest(self):
        return 0.0
    def __add__(self, other):
        return self._balance + other._balance
class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05   
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02  
savings = SavingsAccount("Ravi", 10000)
current = CurrentAccount("Anjali", 15000)
print("Savings Account")
print("Name:", savings._name)
print("Balance:", savings._balance)
print("Interest:", savings.calculate_interest())
print()
print("Current Account")
print("Name:", current._name)
print("Balance:", current._balance)
print("Interest:", current.calculate_interest())
print()
total_balance = savings + current
print("Total Balance (Savings + Current):", total_balance)
