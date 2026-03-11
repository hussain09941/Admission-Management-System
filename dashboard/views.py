from django.shortcuts import render,redirect
from .models import Slide, Course
from admission.models import Admission
from students.models import StudentProfile
import random
def home(request):
    slides = Slide.objects.all()
    courses = Course.objects.all()
    return render(request, "home.html", {
        "slides": slides,
        "courses": courses
    })





def approve_admission(request, id):
    admission = Admission.objects.get(id=id)
    admission.status = 'APPROVED'
    admission.save()

    # create student profile
    StudentProfile.objects.create(
        user=admission.user,
        roll_no=f"ROLL{random.randint(1000,9999)}",
        course=admission.course
    )

    return redirect('dashboard:admin_dashboard')