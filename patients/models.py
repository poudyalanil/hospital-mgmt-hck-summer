from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
