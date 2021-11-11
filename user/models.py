from django.db import models

# Create your models here.

class Administer(models.Model):
    GENDER_CHOICES = ('M','F')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    email = models.EmailField()

class User(models.Model):
    GENDER_CHOICES = ('M','F')

    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    email = models.EmailField()
    admin_nubmer = models.ForeignKey(Administer)

