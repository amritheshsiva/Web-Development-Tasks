import random
import math
a=input("Enter names of invited guests :")
a = a.split(",")
names=[]
for i in a:
    i = i.strip()
    if i not in names:
        names.append(i) 
rand=random.choice(names)
rev=rand[::-1]
print("Reversed Name:",rev)
print("Total number of unique names",len(names))
sqr=math.sqrt(len(names))
round=round(sqr)
print(round)

