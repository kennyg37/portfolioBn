# Generated by Django 5.1 on 2024-08-15 15:35

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('subtitle', models.CharField(max_length=1200)),
                ('image', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('commentCount', models.PositiveIntegerField(default=0)),
                ('comments', models.TextField(default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
