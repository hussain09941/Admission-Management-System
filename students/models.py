from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Course

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

#--------------subject models-------------
class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
 #Add rresult model

class Result(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        related_name="results",
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        unique_together = ('student', 'subject') 