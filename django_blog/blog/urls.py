
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]

from django.urls import path
from .views import (
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView,
)

urlpatterns = [
    # Other URL patterns here...
    
    # URL pattern for creating a new comment
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    
    # URL pattern for updating an existing comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    
    # URL pattern for deleting a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]


