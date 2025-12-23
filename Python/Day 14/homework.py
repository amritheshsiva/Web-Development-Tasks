import random
import math
n=input("Enter names of customers :")
n=n.split(",")
system=[]
for i in n:
    i=i.strip()
    if i not in system:
        system.append(i)
random.shuffle(system)
winner=random.sample(system,2)
rev_winners = [name[::-1] for name in winner]
print("Reversed Winners:", rev_winners)
print("Total participants:", len(system))
sqrt=math.sqrt(len(system))
print(sqrt)
print(round(sqrt))