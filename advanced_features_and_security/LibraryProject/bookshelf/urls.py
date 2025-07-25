from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='list_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]