web_dev=["Jishnu","Hemand","Ravi"]
data_science=["Kiran","Sneha","Dev"]
ui_ux=["Arjun","Rahul","Meera"]
all_participants=[web_dev,data_science,ui_ux]
web_dev.append("Vishnu")
data_science.insert(1,"Astle")
ui_ux.pop()
data_copy=data_science.copy()
data_science.clear()
print(web_dev[0:2])
l=[len(i) for i in data_copy]
print(l)
print("Asha" in web_dev or "Asha" in data_copy or "Asha" in ui_ux)
first_participant=(web_dev[0],data_copy[:1][0],ui_ux[0])
