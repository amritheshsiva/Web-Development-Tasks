frontend = {"Rahul", "Hemanth", "Jishnu", "Allen"}
backend = {"Hemanth", "Jishnu", "Kiran", "Varun"}
backend.add("Rahul")
frontend.remove("Varun")  
both_fb = frontend & backend
print("Students in both Frontend and Backend:",both_fb)
only_backend = backend - frontend
print("Students only in Backend:",only_backend)
total_unique = len(frontend | backend)
print("Total unique students:",total_unique)
fb_courses = {"Frontend": len(frontend),"Backend": len(backend)}
for course, count in fb_courses.items():
    print(f"Course: {course}, Students: {count}")
full_courses = {course: count for course, count in fb_courses.items()}
full_courses["Fullstack"] = fb_courses["Frontend"] + fb_courses["Backend"]
print("Courses with Fullstack added:", full_courses)
