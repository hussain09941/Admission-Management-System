from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import StudentRegistratinForm
from django.contrib.auth import authenticate
def register(request):
    if request.method == 'POST':
        form = StudentRegistratinForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username= form.changed_data['username'],
                email= form.changed_data['password']
            )
            login(request,user)
            return redirect('student_dashboard')
    else:
        form = StudentRegistratinForm()
    return render(request,'accounts/register.html',{'form':form})

#   ________________ user login______________
def user_login(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = authenticate(username = username,password =password)

        if user:
            login(request,user)

            if user.profile.role == "ADMIN":

                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')  
    return render(request,'accounts/login.html')
    