a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if (a>b) and (a>c):
    print("{0} is greater than {1} and {2}".format(a,b,c))
elif(b>a)and (b>c):
    print("{0} is greater than {1} and {2}".format(b,a,c))
else:
    print("{0} is greater than {1} and {2}".format(c,a,b))