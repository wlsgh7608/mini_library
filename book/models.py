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
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)


class AddBook(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    manager_id = models.ForeignKey(Manager,on_delete=models.CASCADE)

class BookMark(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)

class Review(models.Model):
    writer = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    rate = models.FloatField()
    date = models.DateField()
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)

class WriteReview(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    review_id = models.ForeignKey(Review,on_delete=models.CASCADE)