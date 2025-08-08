from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


# ViewSet protected by token-based auth
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = BookSerializer
    queryset = Book.objects.all()