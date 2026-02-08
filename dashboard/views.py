from django.shortcuts import render
from .models import Slide, Course

def home(request):
    slides = Slide.objects.all()
    courses = Course.objects.all()
    return render(request, "home.html", {
        "slides": slides,
        "courses": courses
    })
