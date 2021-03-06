# Generated by Django 3.2.12 on 2022-05-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_alter_feed_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='hashtag',
            field=models.ManyToManyField(blank=True, to='feeds.Hashtag'),
        ),
    ]
