from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images', default='profile.png')