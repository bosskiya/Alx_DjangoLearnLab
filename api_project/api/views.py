from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()