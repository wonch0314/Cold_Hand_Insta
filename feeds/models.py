from tkinter import CASCADE
from django.db import models
from insta import settings

# Create your models here.
class Feed(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.ImageField(null=True, blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='feed_users'
    )

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_feeds'
    )
    
    bookmark_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='bk_feed'
    )

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_users'
    )

    feed = models.ForeignKey(
        Feed,
        on_delete=models.CASCADE,
        related_name='feeds'
    )