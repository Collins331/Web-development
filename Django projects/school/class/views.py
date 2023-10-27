from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'navbar': 'home'})

def addstudent(request):
    return render(request, 'addstudent.html', {'navbar': 'add'})

def viewdata(request):
    return render(request, 'viewdata.html', {'navbar': 'data'})

def about(request):
    return render(request, 'about.html', {'navbar': 'about'})