from django.urls import path
from .views import DoctorListView

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor_list'),
]
