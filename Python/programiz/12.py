l=int(input("Enter a year:"))
if (l%400==0)and (l%100==0):
    print("It is a leap year")
elif (l%4==0)and (l%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")