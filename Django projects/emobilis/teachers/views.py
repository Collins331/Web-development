from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to emobilis")

def about(request):
    return HttpResponse("about emobilis")

def courses(request):
    return HttpResponse("eMobilis offers various cousres including: Web development, Fullstack development, Data Analysis, and Data Science")