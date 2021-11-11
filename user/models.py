from django.db import models

# Create your models here.

class Manager(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female')
        )
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    email = models.EmailField()

class User(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female')
        )

    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    email = models.EmailField()
    admin_nubmer = models.ForeignKey(Manager,on_delete=models.CASCADE)

class Manage(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    manager_id = models.ForeignKey(Manager,on_delete=models.CASCADE)