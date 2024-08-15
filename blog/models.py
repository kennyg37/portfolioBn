import uuid
from django.db import models

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=1200)
    image = models.TextField(default='')
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    commentCount = models.PositiveIntegerField(default=0)
    comments = models.TextField(default='')
    author = models.ForeignKey('authentication.MyUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
