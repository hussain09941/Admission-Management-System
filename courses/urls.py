from django.urls import path
from . import views

urlpatterns = [
    # Example route
    path('', views.course_list, name='course_list'),
]