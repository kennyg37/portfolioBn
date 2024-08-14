from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True)  

    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name', 'password', 'role']  
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def create(self, validated_data):
        role = validated_data.pop('role', 'user')  
        is_staff = True if role == 'admin' else False
        
        user = MyUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=is_staff,
        )
        return user
