python = {"Rahul", "Hemanth", "Jishnu", "Allen"}
data_science = {"Hemanth", "Jishnu", "Kiran", "Varun"}
python.add("Arjun")
data_science.remove("Varun")  
both = python & data_science
print("Students in both Python and Data Science:",both)
only_python = python - data_science
print("Students only in Python:",only_python)
combined = python | data_science
print("All unique students in either course:",combined)
courses = {"Python": len(python),"Data Science": len(data_science)}
for course, count in courses.items():
    print(f"Course: {course}, Students: {count}")
growth = {course: count*2 for course,count in courses.items()}
print("Expected growth (values doubled):",growth)
