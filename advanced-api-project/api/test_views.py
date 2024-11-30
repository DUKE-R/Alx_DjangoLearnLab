from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2021)
        # Authenticate the user
        self.client.login(username="testuser", password="testpassword")

    def test_list_books(self):
        # Test retrieving all books
        response = self.client.get(reverse('book-list'))  # Replace 'book-list' with your view name
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        # Test creating a new book
        data = {"title": "New Book", "author": "Author C", "publication_year": 2022}
        response = self.client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        # Test updating a book
        data = {"title": "Updated Book", "author": "Author A", "publication_year": 2020}
        response = self.client.put(reverse('book-detail', args=[self.book1.id]), data)  # Replace with your view name
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        # Test filtering books by publication_year
        response = self.client.get(reverse('book-list'), {'publication_year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        # Test searching books by title
        response = self.client.get(reverse('book-list'), {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        # Test ordering books by title
        response = self.client.get(reverse('book-list'), {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')
