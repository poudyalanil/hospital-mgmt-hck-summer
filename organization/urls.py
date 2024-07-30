from django.urls import path
from .views import company_list,company_create,company_update, login_view

urlpatterns = [
    path('companies/', company_list, name='company-list'),
    path('companies/create/', company_create, name='company-create'),
    path('companies/<int:pk>/', company_update, name='company-update'),
    path('login/', login_view, name='token_obtain_pair'),

]