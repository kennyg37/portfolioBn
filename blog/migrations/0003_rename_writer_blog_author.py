# Generated by Django 5.1 on 2024-08-14 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_commentcount_blog_comments_blog_likes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='writer',
            new_name='author',
        ),
    ]
