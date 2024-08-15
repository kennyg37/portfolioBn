from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('data/', BlogListView.as_view(), name='blog-list'),
    path('data/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]