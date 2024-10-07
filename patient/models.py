from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    insurance_policy_number = models.CharField(max_length=100, blank=True, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    medical_history = models.TextField(blank=True, null=True)  # Previous medical conditions
    allergies = models.TextField(blank=True, null=True)  # Known allergies

    # Optional: You can add a profile picture or image field
    profile_picture = models.ImageField(upload_to='patient_profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
