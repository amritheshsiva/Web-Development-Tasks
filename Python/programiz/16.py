f=int(input("Enter a number:"))
fact=1
if f<0:
    print("No factorial")
elif (f==0):
    print("The factorial is 1")
else:
    for i in range(1,f+1):
        fact=fact*i
        print(fact)