from django.shortcuts import render

def employee_directory(request):
    employees = [
        {"name": "Amit", "title": "Software Developer", "salary": 50000, "fullTime": True},
        {"name": "Sneha", "title": "UI Designer", "salary": 35000, "fullTime": False},
        {"name": "Rahul", "title": "Tester", "salary": 30000, "fullTime": True},
    ]

    return render(request, "index.html", {"employees": employees})
