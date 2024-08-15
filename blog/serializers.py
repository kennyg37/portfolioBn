from rest_framework import serializers
from .models import Blog
from authentication.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None
        if user is None:
            raise serializers.ValidationError("User must be authenticated to create a blog.")
        validated_data['author'] = user
        return super().create(validated_data)
