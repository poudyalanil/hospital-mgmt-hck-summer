
from django import forms
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'reason']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.all()
        self.fields['doctor'].queryset = Doctor.objects.all()
