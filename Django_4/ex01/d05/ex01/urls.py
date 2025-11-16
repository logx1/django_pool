from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from .views import djnago_templ, display_templ

def hello_word(request):
    return render(request, 'django.html')


urlpatterns = [ 
    path('/django', djnago_templ),
    path('/display', display_templ)
]