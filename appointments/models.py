from django.db import models
from patients.models import Patient
from doctors.models import Doctor
# Create your models here.

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"
