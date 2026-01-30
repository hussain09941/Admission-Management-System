
from django.db import models
from admission.models import AdmissionForm

class Payment(models.Model):
    admission = models.OneToOneField(AdmissionForm, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_id} - {self.status}"

