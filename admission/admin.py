from django.contrib import admin
from .models import AdmissionForm

#admin.site.register(AdmissionForm)
@admin.register(AdmissionForm)
class AdmissionAdmin(admin.ModelAdmin):
    list_display =('id','first_name','last_name','email','course','photo','created_at')
    list_filter = ('course',)
    search_fields=('name','email')