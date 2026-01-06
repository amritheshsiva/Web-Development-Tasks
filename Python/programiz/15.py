a=int(input("Enter starting of interval:"))
b=int(input("Enter ending of interval:"))
print("The prime numbers between {0} and {1} are".format(a,b))
for i in range(a,b):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i)