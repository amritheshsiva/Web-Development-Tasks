a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 
op=input("Choose Operations (+,-,/,*) : ")  
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero"
c = Calculator()
if op=="+":
    print("Addition:",c.add(a, b))
elif op=="-":
    print("Subtraction:",c.subtract(a, b))
elif op=="*":
    print("Multiplication:",c.multiply(a, b))
else:
    print("Division:",c.divide(a, b))
