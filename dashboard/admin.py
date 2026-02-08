from django.contrib import admin
from .models import Slide, Course


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration')
    search_fields = ('name',)
