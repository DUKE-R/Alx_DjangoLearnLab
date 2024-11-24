from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    """
    API view to retrieve a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
