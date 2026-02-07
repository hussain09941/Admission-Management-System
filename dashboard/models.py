from django.db import models

class Slide(models.Model):

    image = models.ImageField(upload_to="slides/")

    def __str__(self):

        return "Slide Image"