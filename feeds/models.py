from django.db import models
from insta import settings

# Create your models here.
class Feed(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.TextField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='feed_users'
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