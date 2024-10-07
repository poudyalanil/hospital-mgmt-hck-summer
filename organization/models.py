from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')  # Requires Pillow
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialization}"


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('Scheduled', 'Scheduled'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')])

    def __str__(self):
        return f"Appointment of {self.patient} with {self.doctor} on {self.appointment_date}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medical_records')
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.patient} by {self.doctor} on {self.date_created}"
