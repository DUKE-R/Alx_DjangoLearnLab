# CRUD Operations for Book Model

This document outlines the commands used to perform Create, Retrieve, Update, and Delete (CRUD) operations on the `Book` model in the Django shell.

---

## 1. Create Operation
**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

book.title = "Nineteen Eighty-Four"
book.save()
print(book)

book.delete()
books = Book.objects.all()
print(books)

