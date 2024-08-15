from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from blog.imageUpload import UploadImageToS3Mixin
from ..models import Blog
from ..serializers import BlogSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import boto3
from rest_framework.parsers import MultiPartParser, FormParser


class BlogListView(APIView, UploadImageToS3Mixin):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        queryset = Blog.objects.filter(author=request.user)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        image = request.data.get('image')
        if image:
            image_url = self.upload_image_to_s3(image)
            request.data['image'] = image_url

        serializer = BlogSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(APIView, UploadImageToS3Mixin):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if instance is None or instance.author != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if instance is None or instance.author != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BlogSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if instance is None or instance.author != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BlogSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if instance is None or instance.author != request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogOperationsView(APIView):
    parmission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    
