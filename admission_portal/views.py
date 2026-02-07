from django.shortcuts import render
from dashboard.models import Slide

def home(request):
    slides = Slide.objects.all()
    return render(request, "home.html", {"slides": slides})