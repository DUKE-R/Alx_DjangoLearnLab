from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.views.generic.detail import DetailView
from .models import Library

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app/register.html')  # Replace 'home' with the appropriate URL name
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if user is an admin
def is_admin(user):
    return user.userprofile.role == 'Admin'
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Helper function to check if user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Helper function to check if user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view (only accessible by Admin users)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian view (only accessible by Librarian users)
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view (only accessible by Member users)
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')


from django.shortcuts import redirect

@user_passes_test(is_admin, login_url='/not-authorized/')
def admin_view(request):
    return render(request, 'admin_view.html')



from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if the user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Librarian view (only accessible by Librarian users)
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')



from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if the user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

# Member view (only accessible by Member users)
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

# In views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # Assuming you have a form for adding/editing books

# Add Book View (Only users with 'can_add_book' permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list page
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Edit Book View (Only users with 'can_change_book' permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list page
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

# Delete Book View (Only users with 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list page
    return render(request, 'delete_book.html', {'book': book})

# In relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Helper functions to check roles
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - only accessible to users with the 'Admin' role
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - only accessible to users with the 'Librarian' role
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - only accessible to users with the 'Member' role
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')




