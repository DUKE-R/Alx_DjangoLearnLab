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


