from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html', )

def contact(request):
    return render(request, 'pages/contact.html')

def service(request):
    return render(request, 'service.html')