from django.urls import path
from .views import AppointmentListView

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment_list'),
]
