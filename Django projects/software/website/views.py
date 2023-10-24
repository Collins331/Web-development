from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to our Website")

def hello(request):
    return render(request, "hello.html", {'name': 'Collins'})