from django.urls import path,include
from .views import BookList,BookDetail, BookMarkList,BookReview,BookDataUpdate,AddNewBook
"""
BASE ENDPOINT  book/
"""

urlpatterns = [
    path('list/',BookList.as_view()), # book list
    path('detail/<int:isbn>/',BookDetail.as_view()), #book detail

    path('review/<int:isbn>/',BookReview.as_view()),
    path('update/',BookDataUpdate.as_view()),
    path('bookmark/',BookMarkList.as_view()), # bookmark

    path('addbook/',AddNewBook.as_view())
    
]
