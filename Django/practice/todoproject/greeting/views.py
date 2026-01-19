from django.shortcuts import render
from .models import Customer
from .forms import LoginForm

def greeting(request):
    if request.method == "POST":
        form=LoginForm(request.POST)

        if form.is_valid():
            cust=Customer()
            cust.email=form.cleaned_data['email']
            cust.password=form.cleaned_data['password']
            cust.save()
            return render(request,'result.html',{
                'message':'Data Saved!!'
            })
        
    else:
        form=LoginForm()
    return render(request,'index.html',{'form':form})