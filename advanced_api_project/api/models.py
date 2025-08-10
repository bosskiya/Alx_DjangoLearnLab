from django.db import models


# Author model represents the writer of books.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Book model represents a published book, linked to an Author.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title