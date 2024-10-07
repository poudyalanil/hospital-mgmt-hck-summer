from django.views.generic import ListView
from .models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'
