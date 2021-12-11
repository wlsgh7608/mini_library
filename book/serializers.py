from .models import *
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title','author','publisher','isbn')

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddBook
        fields = '__all__'

class BookMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookMark
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField()
    date = serializers.ReadOnlyField()
    class Meta:
        model = Review
        fields = ('id','writer','title','rate','date','content')

class WriteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteReview
        fields = '__all__'
        


