from django.db import models
from insta import settings

# Create your models here.
class Hashtag(models.Model):
    content = models.CharField(max_length=10)

class Feed(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.ImageField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_feeds'
    )

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_feeds'
    )

    hashtag = models.ManyToManyField(
        Hashtag,
        blank=True,
        related_name='hashtag_feeds'
    )

    tag_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='tag_feeds'
    )

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_comments'
    )

    feed = models.ForeignKey(
        Feed,
        on_delete=models.CASCADE,
        related_name='feed_comments'
    )