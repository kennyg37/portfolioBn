from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..models import Blog
from ..serializers import BlogSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class BlogOperationsView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return None

    def post(self, request, pk, *args, **kwargs):
        action = request.data.get('action')
        instance = self.get_object(pk)
        
        if instance is None:
            return Response({'detail': 'Blog not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if action == 'like':
            instance.likes += 1
            instance.save()
            return Response({'likes': instance.likes}, status=status.HTTP_200_OK)
        
        elif action == 'unlike':
            if instance.likes > 0:
                instance.likes -= 1
                instance.save()
            return Response({'likes': instance.likes}, status=status.HTTP_200_OK)
        
        elif action == 'comment':
            comment = request.data.get('comment')
            if not comment:
                return Response({'detail': 'Comment cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)
            instance.comments += comment + '\n'  # Append the new comment
            instance.commentCount += 1
            instance.save()
            return Response({
                'comments': instance.comments,
                'commentCount': instance.commentCount
            }, status=status.HTTP_200_OK)
        
        else:
            return Response({'detail': 'Invalid action.'}, status=status.HTTP_400_BAD_REQUEST)
