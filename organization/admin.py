from django.contrib import admin
from .models import Company, Department, Doctor, Patient, Appointment, MedicalRecord

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
