from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.request.user.notifications.all()

    def post(self, request, *args, **kwargs):
        notifications = self.request.user.notifications.filter(read=False)
        notifications.update(read=True)
        return Response({"message": "All notifications marked as read"}, status=200)
