# Generated by Django 3.2.12 on 2022-05-08 06:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0010_feed_tag_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='bookmark_user',
            field=models.ManyToManyField(blank=True, null=True, related_name='bk_feed', to=settings.AUTH_USER_MODEL),
        ),
    ]
