from django.db import models
from users.models import  Manager
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()
class Book(models.Model):
    isbn = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=512)
    price = models.IntegerField()

    author = models.CharField(max_length=256)
    link_url = models.CharField(max_length=256,default='')
    image_url = models.CharField(max_length=256,default = '')
    pubdate = models.DateField()
    publisher = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)


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
    content = models.TextField()
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)

class WriteReview(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    review_id = models.ForeignKey(Review,on_delete=models.CASCADE)