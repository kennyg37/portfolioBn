from django.urls import path
from .views import BlogViewSet

urlpatterns = [
    path('blog/', BlogViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]