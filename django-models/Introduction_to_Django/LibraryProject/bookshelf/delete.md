# Delete Operation for Book Model

**Command:**
```python
from bookshelf.models import Book

# Retrieve the book instance you want to delete
book = Book.objects.get(title="1984")
book.delete()

# Check if the book has been deleted
books = Book.objects.all()
print(books)
