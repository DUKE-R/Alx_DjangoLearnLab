# relationship_app/urls.py
from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # URL for function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based view
]


from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

# In urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
]

# In urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('librarian/', views.librarian_view, name='librarian_view'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.member_view, name='member_view'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('book/add/', views.add_book, name="add_book/"),  # Add book view
    path('book/edit/<int:pk>/', views.edit_book, name="edit_book/"),  # Edit book view with primary key (pk) for identifying the book
    path('book/delete/<int:pk>/', views.delete_book, name="delete_book/"),  # Delete book view
]

