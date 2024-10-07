from django.urls import path
from .views import PatientListView

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
]
