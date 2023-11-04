from django.shortcuts import render, redirect
from .models import Student, Slider
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    data = Student.objects.all()

    return render(request, 'home.html', {'navbar': 'home', 'data': data})

def addstudent(request):
    return render(request, 'addstudent.html', {'navbar': 'add'})

def viewdata(request):
    paginator = Paginator(Student.objects.all(), 5)
    new_page = request.GET.get('page')
    student = paginator.get_page(new_page)
    return render(request, 'viewdata.html', {'navbar': 'data', 'data': student})

def about(request):

    return render(request, 'about.html', {'navbar': 'about'})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/viewdata")

def insert(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        if len(request.FILES["image"]) != 0:
            image = request.FILES["image"]

        room = Student(name=name, email=email, age=age, image=image)
        room.save()
        messages.success(request, 'Data added successfully')
        return redirect("/viewdata")
    return redirect("/viewdata")


def edit(request, id):
    std = Student.objects.get(id=id)
    cont = {'ids': std}
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        student = Student.objects.get(id=id)

        if len(request.FILES) != 0:
            if student.image > 0:
                student.image = request.FILES['image']

        student.name = name
        student.email = email
        student.age = age

        student.save()
        messages.warning(request, 'Data edited successfully')
        return redirect("/viewdata")
    return render(request, 'edit.html', cont)


def sliders(request):
    slide = Slider.objects.all()
    return render(request, 'slider.html', {'slider': slide, 'navbar': 'slide'})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            std = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(age__icontains=query))
            return render(request, 'search.html', {'data': std, 'query': query})
    return render(request, 'search.html')
