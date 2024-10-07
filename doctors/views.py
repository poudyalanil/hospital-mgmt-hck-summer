from django.views.generic import ListView
from .models import Doctor

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'
    context_object_name = 'doctors'
