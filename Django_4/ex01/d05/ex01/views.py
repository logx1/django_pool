from django.shortcuts import render

# Create your views here.

def djnago_templ(request):
    return render(request, 'django.html')

def display_templ(request):
    return render(request, 'display.html')