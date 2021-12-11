from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.db.models.deletion import CASCADE
# Create your models here.


# User = get_user_model()



class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, nickname, password=None):
        user = self.create_user(
            email = email,
            password = password,
            nickname = nickname,
        )
        
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        Manager.objects.create(
            email = email,
        )


        return user

class User(AbstractBaseUser,PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    nickname = models.CharField(
        max_length=20,
        null=False,
    )    
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

class Manager(models.Model):
    email = models.EmailField()

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
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


class Check(models.Model):
    aff = models.CharField(max_length=255)