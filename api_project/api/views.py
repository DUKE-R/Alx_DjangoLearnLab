from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet

class BookList(generics.ListAPIView):
    """
    API view to retrieve a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    class BookViewSet(ModelViewSet):
      """
      A viewset that provides the standard actions
      for the Book model (CRUD operations).
      """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
