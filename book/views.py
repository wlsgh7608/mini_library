from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView



from book.serializers import BookSerializer, ReviewSerializer,BookDetailSerializer
# Create your views here.
from .models import Book, Review
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote

import json
from datetime import datetime

class BookList(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many= True)
        return Response(serializer.data)

    def post(self,request):
        print(request.data)
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response({"message":"good"},status =200)

class BookDetail(APIView):
    def get(self,request,book_id):
        book = Book.objects.filter(id=book_id).exists
        if book:
            book = Book.objects.get(id=book_id)
            serializer = BookDetailSerializer(book)
            return Response(serializer.data)
        else:
            return Response({"message":"book does not exit"},status= 404)

class BookReview(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self,book_id):
        return self.queryset.filter(book_id = book_id)

    def post(self, request, book_id,*args, **kwargs):
        return self.create(request)



class BookDataUpdate(APIView):
    
    
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



