from django.urls import path
from .views.views import BlogListView, BlogDetailView
from .views.operations import BlogOperationsView

urlpatterns = [
    path('data/', BlogListView.as_view(), name='blog-list'),
    path('data/<uuid:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('data/<uuid:pk>/operations/', BlogOperationsView.as_view(), name='blog-operations')
]