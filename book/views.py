from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView



from book.serializers import BookSerializer, ReviewSerializer
# Create your views here.
from .models import Book, Review

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
            serializer = BookSerializer(book)
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

"""
def get(self,request,book_id):
    해당 책에 해당하는 Review
    reviews = Review.objects.filter(book_id = book_id)
    serializer = ReviewSerializer(reviews, many= True)
    return Response(serializer.data)

def post(self,request,book_id):
    해당 책 reivew 생성
"""



