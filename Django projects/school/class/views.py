from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def home(request):
    data = Student.objects.all()

    return render(request, 'home.html', {'navbar': 'home', 'data': data})

def addstudent(request):
    return render(request, 'addstudent.html', {'navbar': 'add'})

def viewdata(request):
    student = Student.objects.all()
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
        return redirect("/viewdata")
    return render(request, 'edit.html', cont)
