from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import StudentRegistratinForm

def register(request):
    if request.method == 'POST':
        form = StudentRegistratinForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentRegistratinForm()

    return render(request, 'accounts/register.html', {'form': form})


#   ________________ user login______________
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.profile.role == "ADMIN":
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')

    return render(request, 'accounts/login.html')
