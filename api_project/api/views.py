from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer


class BookList(ListAPIView):
    http_method_names = ('patch', 'get')
    permission_classes = [permissions.AllowAny,]
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()