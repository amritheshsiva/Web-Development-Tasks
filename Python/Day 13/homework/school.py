n=int(input("Enter the number of students:"))
f=open("students.txt","a")
for i in range(n):
    name=input("Enter name:")
    f.write(name+"\n")
f.close()
f=open("students.txt","r")
print(f.read())




