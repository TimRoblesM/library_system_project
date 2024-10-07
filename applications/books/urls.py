from django.urls import path
from . import views

urlpatterns = [
    path('books/list/', views.BookListAPIView.as_view(), name='books_list'),
]