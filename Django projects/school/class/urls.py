from django.urls import path
from . import views

app_name = "class"
urlpatterns = [
    path("", views.home, name='home'),
    path("addstudent", views.addstudent, name='add-student'),
    path("viewdata", views.viewdata, name='view-data'),
    path("about", views.about, name='about'),
    path("delete/<id>", views.delete, name='delete'),
    path("insert", views.insert, name='insertdata'),
    path("edit/<id>", views.edit, name='edit'),
    path("sliders", views.sliders, name='slider'),
]