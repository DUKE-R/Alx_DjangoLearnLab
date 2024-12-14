from django.shortcuts import render
from rest_framework import generics

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# posts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Post, Like
from notifications.models import Notification

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = generics.get_object_or_404(Post, id=pk)
        user = request.user

        if Like.objects.filter(user=user, post=post).exists():
            return Response({"message": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        like = Like.objects.get_or_create(user=request.user, post=post)

        # Create a notification for the post owner
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post
            )

        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        user = request.user

        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
