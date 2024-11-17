from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to list all books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# View to display details of a single book
@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

# View to create a new book
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        genre = request.POST['genre']
        
        book = Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            genre=genre
        )
        return render(request, 'book_detail.html', {'book': book})
    
    return render(request, 'book_create.html')

# View to edit an existing book
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.genre = request.POST['genre']
        book.save()
        return render(request, 'book_detail.html', {'book': book})
    
    return render(request, 'book_edit.html', {'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.delete()
        return render(request, 'book_list.html', {'books': Book.objects.all()})
    
    return render(request, 'book_confirm_delete.html', {'book': book})

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.shortcuts import get_list_or_404
from bookshelf.models import Book

def safe_view(request):
    title = request.GET.get('title', '').strip()
    books = get_list_or_404(Book, title__iexact=title)
    return render(request, 'bookshelf/book_list.html', {'books': books})
