from django.contrib import admin
from .models import Admission
from django.contrib import admin
from django.utils.html import format_html
# from .models import Admission

#admin.site.register(AdmissionForm)
@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display =('id','first_name','last_name','email','course','photo','created_at')
    list_filter = ('course',)
    search_fields=('name','email')

    list_display = (
        "admission_id",
        "first_name",
        "student_phone",
        "course",
        "status",
        "photo_preview"
    )

    list_filter = ("status", "course")
    search_fields = ("admission_id", "first_name", "student_phone")

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:5px;" />',
                obj.photo.url
            )
        return "No Photo"

    photo_preview.short_description = "Photo"    