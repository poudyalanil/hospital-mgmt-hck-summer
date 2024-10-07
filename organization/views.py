
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Company


def home(request):
    return render (request, 'login.html')
