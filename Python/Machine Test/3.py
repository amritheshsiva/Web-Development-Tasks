a = [{"id": 1, "name": "rajesh"},{"id": 2, "name": "rahul"},{"id": 3, "name": "sruthi"}]
id_no = int(input("Enter student id: "))
for i in a:
    if i["id"] == id_no:
        print("Student name:", i["name"])
        break
else:
    print("Student not found")

    