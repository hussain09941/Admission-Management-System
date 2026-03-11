from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from .forms import StudentRegistratinForm
from students.models import StudentProfile
from django.contrib.auth.decorators import login_required



# ____________ Register view ____________
def register(request):
    if request.method == 'POST':
        form = StudentRegistratinForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # create student profile automatically
            StudentProfile.objects.create(user=user)

            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentRegistratinForm()

    return render(request, 'accounts/register.html', {'form': form})


# ____________ Login view ____________
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            # create profile if missing
            StudentProfile.objects.get_or_create(user=user)

            login(request, user)
            return redirect('student_dashboard')

    return render(request, 'accounts/login.html')
# logout 

@login_required
def log_out(request):
    logout(request)
    return redirect('accounts:login')




