from django.urls import path
from . import views

app_name = "class"
urlpatterns = [
    path("", views.home, name='home'),
    path("addstudent", views.addstudent, name='add-student'),
    path("viewdata", views.viewdata, name='view-data'),
    path("about", views.about, name='about')
]