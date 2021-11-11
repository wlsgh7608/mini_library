from django.db import models
from user.models import  Manager,User
# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=15)
    category = models.CharField(max_length=50)
    publish_date = models.DateField()
    publisher = models.CharField(max_length=50)
    


class Author(models.Model):
    name = models.CharField(max_length=15)
    birthday = models.DateField()


class Publish(models.Model):
    author_seq = models.ForeignKey(Author)
    book_seq = models.ForeignKey(Book)


class AddBook(models.Model):
    book_seq = models.ForeignKey(Book)
    manager_seq = models.ForeignKey(Manager)

class BookMark(models.Model):
    user_seq = models.ForeignKey(User)
    book_seq = models.ForeignKey(Book)