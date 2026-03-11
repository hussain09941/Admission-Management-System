# from django.db import models
# from django.contrib.auth.models import User
# from courses.models import Course


# class AdmissionForm(models.Model):

#     STATUS_CHOICES = (
#         ('PENDING', 'Pending'),
#         ('APPROVED', 'Approved'),
#         ('REJECTED', 'Rejected'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=10)
#     email = models.EmailField()

#     # ✅ Add photo
#     photo = models.ImageField(upload_to='admission_photos/')

#     # Optional but professional
#     created_at = models.DateTimeField(auto_now_add=True)

#     status = models.CharField(
#         max_length=10,
#         choices=STATUS_CHOICES,
#         default='PENDING'
#     )

#     def __str__(self):
#         return f"{self.first_name} - {self.status}"



from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
import os


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="batches")
    timing = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.course.name} - {self.timing}"


class Admission(models.Model):

    # ================= Admission ID =================
    admission_id = models.CharField(max_length=15, unique=True, blank=True)

    # ================= Student Details =================
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    student_email = models.EmailField(unique=True)

    phone_validator = RegexValidator(
        regex=r'^[6-9]\d{9}$',
        message="Enter a valid 10-digit Indian phone number"
    )
    student_phone = models.CharField(
        max_length=10,
        validators=[phone_validator],
        unique=True
    )

    student_dob = models.DateField()

    # ================= Parent Details =================
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    guardian_phone = models.CharField(
        max_length=10,
        validators=[phone_validator]
    )

    # ================= Address =================
    home_address = models.CharField(max_length=150)
    post_office = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    # ================= Documents =================
    photo = models.ImageField(upload_to="admissions/photos/")
    aadhaar_document = models.FileField(upload_to="admissions/documents/")

    # ================= Course Info =================
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True)

    # ================= Status =================
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    created_at = models.DateTimeField(auto_now_add=True)

    # ================= Auto Generate Admission ID =================
    def save(self, *args, **kwargs):
        if not self.admission_id:
            year = timezone.now().year
            last_record = Admission.objects.filter(
                admission_id__startswith=f"ADM{year}"
            ).order_by("-admission_id").first()

            if last_record:
                last_number = int(last_record.admission_id[-3:])
                new_number = last_number + 1
            else:
                new_number = 1

            self.admission_id = f"ADM{year}{str(new_number).zfill(3)}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.admission_id} - {self.first_name} {self.last_name}"
    



    

    def validate_pdf(value):
        ext = os.path.splitext(value.name)[1]
        if ext.lower() != '.pdf':
            raise ValidationError("Only PDF files are allowed.")
    aadhaar_document = models.FileField(
    upload_to="admissions/documents/",
    validators=[validate_pdf]
)    