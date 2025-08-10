from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer handles serialization of individual Book objects.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure publication year is not in the future.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer includes a nested list of books using BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

"""
Explanation:
- `books = BookSerializer(...)` maps the reverse ForeignKey from Author to Book.
- We use the `related_name='books'` on the ForeignKey to access the books easily from the Author object.
- The `read_only=True` ensures that books are serialized in GET operations but not writable via this serializer.
"""
