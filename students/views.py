from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudentProfile

@login_required
def student_dashboard(request):
    profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'students/dashboard.html', {'profile': profile})
