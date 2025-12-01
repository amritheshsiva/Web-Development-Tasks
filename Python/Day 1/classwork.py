import random
apple=15.5
orange=20
grape=10.25
total=apple+orange+grape
print("Total volume sold",total)
print("Total volume in integer is",int(total))
print("Total volume of juice sold is",str(total))
additional= random.randrange(5,10)
final_total=total+additional
print("Final Total volume of juice sold",final_total)
