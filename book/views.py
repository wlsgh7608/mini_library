from time import timezone
# from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView


from book.serializers import BookSerializer, ReviewSerializer,BookDetailSerializer, AddBookSerializer,BookMarkSerializer
from core.utils import LoginConfirm
# Create your views here.
from .models import AddBook, Book, Review, WriteReview,BookMark
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote

import json
from datetime import datetime
from django.utils import timezone
# User = get_user_model()
from users.models import Manager, User


class BookList(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many= True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response({"message":"good"},status =200)

class BookDetail(APIView):
    def get(self,request,isbn):
        book = Book.objects.filter(isbn=isbn).exists()
        if book:
            book = Book.objects.get(isbn=isbn)
            serializer = BookDetailSerializer(book)
            return Response(serializer.data)
        else:
            return Response({"message":"book does not exit"},status= 404)

class BookMarkList(APIView):
    @LoginConfirm
    def get(self,request,):
        bookmark = BookMark.objects.filter(user_id = request.id)
        if bookmark:
            serializer = BookMarkSerializer(bookmark,many= True)
            return Response(serializer.data)
        else:
            return Response({"message":"not found any bookmark"},status = 404)
    @LoginConfirm
    def post(self,request):
        isbn = request.data['isbn']
        if Book.objects.filter(isbn = isbn).exists():
            user = User.objects.get(pk= request.id)
            book = Book.objects.get(isbn = isbn)
            if BookMark.objects.filter(user_id = user).filter(book_id=book): # 해당 북마크 존재
                return Response({"message" : "that book already bookmarked"})

            # 북마크 생성
            BookMark.objects.create(
                user_id = user,
                book_id = book,
            )
            return Response({"message":"bookmark success"})

        return Response({"message":"isbn does not match"},status= 404)


class AddNewBook(APIView):

    @LoginConfirm
    def post(self,request):
        if request.user.is_admin == True:
            serializer = BookDetailSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                user = Manager.objects.get(email = request.user.email)
                book = Book.objects.last()
                AddBook.objects.create(
                    book_id = book,
                    manager_id = user,
                )
                return Response({"message":"Addbook success"},status = 201)
            return Response(serializer.errors,status = 400)
        else:
            return Response({"message": "that user isn't admin"},status= 400)





class BookReview(APIView):
    def get(self,request,isbn,*args,**kwags):
        # 해당 책 북마크목록
        isexist = Book.objects.filter(isbn=isbn).exists()
        if isexist:
            book_id = Book.objects.get(isbn = isbn)
            reviews = Review.objects.filter(book_id = book_id)
            serializer = ReviewSerializer(reviews,many=True)
            return Response(serializer.data)
        return Response({"message":"isbn does not exist"})

    @LoginConfirm
    def post(self, request, isbn,*args, **kwargs):
        # write review
        isexist = Book.objects.filter(isbn=isbn).exists
        if isexist:
            book = Book.objects.get(isbn= isbn)
            serializer = ReviewSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save(writer = request.user.nickname,date = timezone.now(),book_id=book)
                
                user = User.objects.get(id = request.id)
                review = Review.objects.last()
                
                WriteReview.objects.create(
                    user_id = user,
                    review_id = review,
                    book_id = book
                )
                return Response({"message":"good"},status = 201)
            else:
                return Response(serializer.errors)
        return Response({"message":"book id does not exist"},status = 404)



class BookDataUpdate(APIView):
    """
    도서 정보 update
    """
    def get(self,request,*args,**kwargs):
        for i in range(1,6):
            display = 100
            url = 'https://openapi.naver.com/v1/search/book.json?query=it&'+"display=100&"+"start="+str(i*100+1)
            print(url)
            request = Request(url)
            CLIENT_ID = 'i_8pC2lDwjUX3tizVzyP'
            CLIENT_SECRET = 'tVQDEBkV0f'
            request.add_header('X-Naver-Client-Id', CLIENT_ID)
            request.add_header('X-Naver-Client-Secret', CLIENT_SECRET)
            response = urlopen(request).read().decode('utf-8')
            # search_result = json.loads(response)
            search_result = json.loads(response)
            books = search_result['items']
            for j,book in enumerate(books):
                try:
                    print(j)
                    title = book['title']
                    link = book['link']
                    image = book['image']
                    author = book['author']
                    print(book['price'])
                    price = book['price']
                    price = float(price)
                    price = int(price)
                    print(price)
                    publisher = book['publisher']
                    pubdate = book['pubdate']
                    pubdate = datetime.strptime(pubdate, '%Y%m%d')
                    isbn_list = book['isbn']
                    isbn = int(isbn_list.split(' ')[1])
                    description = book['description']
                    description = description.replace('<b>','')
                    description = description.replace('</b>','')
                    if Book.objects.filter(isbn = isbn):
                        continue
                    Book.objects.create(
                        title = title,
                        link_url = link,
                        image_url = image,
                        author = author,
                        price = price,
                        publisher = publisher,
                        pubdate = pubdate,
                        isbn = isbn,
                        description = description,
                    )
                except:
                    continue




            # return search_result
        return 1



"""
def get(self,request,book_id):
    해당 책에 해당하는 Review
    reviews = Review.objects.filter(book_id = book_id)
    serializer = ReviewSerializer(reviews, many= True)
    return Response(serializer.data)

def post(self,request,book_id):
    해당 책 reivew 생성
"""