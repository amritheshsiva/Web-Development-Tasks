des="""Python is a powerful programming language used for web development, data science, automation, and more. 
This course will help beginners understand Python basics and improve problem-solving skills."""
l=len(des)
print("Number of characters :",l)
print("First character in the paragraph is",des[0],"and last character in the paragraph is",des[-2])
short=des[:50]
print("First 50 characters :{}".format(short))
replaced=des.replace("Python","PYTHON")
low=des.lower()
remove=des.strip()
words=des.split(" ")
print("course"in des)
print("The course description is {} characters long and has {} words.".format(l,len(words)))

