from django.urls import path
from .views import list_book, LibraryDetailView

urlpatterns = [
    path('books/', list_book, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
