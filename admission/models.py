from django.db import models
from django.contrib.auth.models import User


class AdmissionForm(models.Model):

    # ---------- STATUS ----------
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    # ---------- STATE ----------
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MH', 'Maharashtra'),
        ('MP', 'Madhya Pradesh'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('TS', 'Telangana'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),

        # Union Territories
        ('AN', 'Andaman & Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra & Nagar Haveli and Daman & Diu'),
        ('JK', 'Jammu & Kashmir'),
        ('LD', 'Lakshadweep'),
        ('LA', 'Ladakh'),
        ('PY', 'Puducherry'),
    ]

    # ---------- COURSE ----------
    COURSE_CHOICES = [
        ('BTECH', 'B.Tech'),
        ('BE', 'B.E'),
        ('BCA', 'BCA'),
        ('BSC', 'B.Sc'),
        ('BCOM', 'B.Com'),
        ('BA', 'B.A'),
        ('BBA', 'BBA'),
        ('MTECH', 'M.Tech'),
        ('MCA', 'MCA'),
        ('MSC', 'M.Sc'),
        ('MCOM', 'M.Com'),
        ('MBA', 'MBA'),
        ('PHD', 'Ph.D'),
        ('DIPLOMA', 'Diploma'),
        ('CERT', 'Certificate'),
    ]


       #------------------Gender Choice-----------------
    gender_choice =[
        ('MALE','Male'),
        ('FEMALE','Female'),
        ('OTHER','Other'),
    ]
    # ---------- BASIC DETAILS ----------
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)

    aadhaar_no = models.CharField(max_length=12, unique=True)
     
    Gender = models.CharField(max_length=6,choices=gender_choice,default='Male')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='photos/')

    # ---------- ADDRESS ----------
    address = models.TextField()
    police_station = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    post_office = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)

    # ---------- STATUS ----------
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"
