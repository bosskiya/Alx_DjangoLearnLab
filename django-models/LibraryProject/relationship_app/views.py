from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

def list_book(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    template_name = 'library_detail.html'
    model = Library
    context_object_name = 'library'