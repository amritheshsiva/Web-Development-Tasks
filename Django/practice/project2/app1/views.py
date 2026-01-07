from django.shortcuts import render
def greeting(request):
    count = 23
    return render(request,'index.html',{'count':count})