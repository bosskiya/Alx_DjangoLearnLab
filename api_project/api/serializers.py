from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author']