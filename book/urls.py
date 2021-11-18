from django.urls import path,include
from .views import BookList,BookDetail,BookReview,BookDataUpdate
"""
BASE ENDPOINT  book/
"""

urlpatterns = [
    path('list/',BookList.as_view()), # book list
    path('detail/<int:book_id>/',BookDetail.as_view()), #book detail

    path('review/<int:book_id>/',BookReview.as_view()),
    # path('update/',BookDataUpdate.as_view())
    
]
