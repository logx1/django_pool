from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render


def lol(request):
    return render(request, 'index.html')

urlpatterns = [
    path('ex00', lol)
]