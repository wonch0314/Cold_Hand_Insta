# Generated by Django 3.2.12 on 2022-04-29 06:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0002_alter_feed_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
