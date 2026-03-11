
from django.db import models
from students.models import StudentProfile

class Payment(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        null=True,     # 👈 temporary
        blank=True
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="SUCCESS")
    created_at = models.DateTimeField(auto_now_add=True)