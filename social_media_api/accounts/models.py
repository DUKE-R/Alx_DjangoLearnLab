from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followed_by',
        blank=True
    )

    def __str__(self):
        return self.username
