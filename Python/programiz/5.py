import cmath
a=int(input("Enter coefficient of x2:"))
b=int(input("Enter coefficient of x:"))
c=int(input("Enter constant:"))
d=(b**2)-(4*a*c)
s1=(-b+cmath.sqrt(d))/(2*a)
s2=(-b-cmath.sqrt(d))/(2*a)
print("The solutions are {0}{1}".format(s1,s2))