from django.shortcuts import render

def student_list(request):
    students = [
        {"name": "Anu", "grade": "A", "passed": True},
        {"name": "Rahul", "grade": "C", "passed": False},
        {"name": "Meera", "grade": "B", "passed": True},
    ]

    return render(request, "students.html", {"students": students})
