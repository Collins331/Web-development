from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images', default='profile.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="Web development teacher")

    def __str__(self):
        return self.name

class Slider(models.Model):
    text1 = models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', default='profile.png')

    def __str__(self):
        return self.text1