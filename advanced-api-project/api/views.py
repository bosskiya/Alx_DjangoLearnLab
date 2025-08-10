from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, BasePermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Read-only for everyone, write access only to admin users.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

# View for listing all books (read-only, open to public)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

    # Add filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    
    # Filtering parameters via query string
    filterset_fields = ['title', 'author', 'publication_year']

    # Searchable fields (text match)
    search_fields = ['title', 'author__name']

    # Fields that can be used for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

# View for retrieving a single book by ID (read-only, open to public)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

# View for creating a new book (write permission required)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]  # Only logged-in users

# View for updating an existing book (write permission required)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        # You could log user or modify data here
        serializer.save()

# View for deleting a book (write permission required)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

"""
View Documentation:

1. BookListView - Lists all books in the database (public access).
2. BookDetailView - Retrieves a single book using its ID (public access).
3. BookCreateView - Allows authenticated users to create a new book.
    - Uses serializer validation to check for future publication years.
4. BookUpdateView - Allows authenticated users to update a book.
5. BookDeleteView - Allows authenticated users to delete a book.

Security:
    - Create/Update/Delete views require login (via IsAuthenticated).
    - Read-only views are open to all users (via AllowAny).
"""
