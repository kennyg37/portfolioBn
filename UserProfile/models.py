from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('authentication.MyUser', on_delete=models.CASCADE)
    bio = models.TextField(default='')
    image = models.TextField(default='')
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
