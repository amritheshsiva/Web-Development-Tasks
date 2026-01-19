from django.shortcuts import render, redirect

students = ['Arun', 'Meena', 'Rahul']

def student_list(request):
    welcome = request.GET.get('msg', 'Welcome Students')
    return render(request, 'students/student_list.html', {
        'students': students,
        'welcome': welcome
    })

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        students.append(name)
        return redirect('/students/?msg=Student added successfully')
    return render(request, 'students/student_form.html')
