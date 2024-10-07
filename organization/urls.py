from django.urls import path

from organization import views
from organization.views import*

urlpatterns = [
    path('', views.home, name='login'),

]