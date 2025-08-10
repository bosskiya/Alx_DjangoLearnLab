"""
Testing Strategy:

- Framework: Django's built-in TestCase with DRF's APITestCase.
- Purpose: Validate CRUD functionality, permissions, and query features (filtering, search, ordering).
- Setup:
    - Creates a user, authors, and sample books.
    - Authenticates when testing protected endpoints.

Endpoints Tested:
- GET /api/books/
- POST /api/books/create/
- PUT /api/books/<pk>/update/
- DELETE /api/books/<pk>/delete/
- Filtering: ?author=
- Searching: ?search=
- Ordering: ?ordering=

Run tests:
    python manage.py test api
"""

from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create test authors
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="Aldous Huxley")

        # Create test books
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author1)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author1)
        self.book3 = Book.objects.create(title="Brave New World", publication_year=1932, author=self.author2)

        self.client = APIClient()

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {
            "title": "Updated Title",
            "publication_year": 1949,
            "author": self.author1.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_filter_books_by_author(self):
        url = reverse('book-list') + f'?author={self.author1.id}'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Animal'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Animal Farm")

    def test_order_books_by_year_desc(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['title'], "New Book" if Book.objects.filter(title="New Book").exists() else "1984")
