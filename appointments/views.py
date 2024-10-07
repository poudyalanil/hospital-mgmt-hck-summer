from django.views.generic import ListView
from .models import Appointment

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'
