from django.db import models

class Slide(models.Model):

    image = models.ImageField(upload_to="slides/")

    def __str__(self):

        return "Slide Image"
    
class Course(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses/')

    def __str__(self):
        return self.name