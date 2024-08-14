from rest_framework import serializers
from .models import Blog
from authentication.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'