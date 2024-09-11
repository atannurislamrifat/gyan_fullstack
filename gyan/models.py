from django.db import models
from django import forms


# Create your models here.


class form(models.Model):
    tid = models.IntegerField()
    f_name = models.CharField(max_length=10)
    l_name = models.CharField(max_length=10)
    number = models.IntegerField()
    mail = models.CharField(max_length=10)
    msg = models.CharField(max_length=10)

class contact_from(models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField()
    subject= models.TextField()
    message= models.TextField()
    


class CustomPasswordResetForm(models.Model):
    username = models.CharField(max_length=150)    
    
    


    