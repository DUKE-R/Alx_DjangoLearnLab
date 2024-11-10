from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Using filter to get all books by this author
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None

# List all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Using filter to get all books in this library
        return library.books.all()
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Accessing the OneToOneField directly to get the librarian
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
