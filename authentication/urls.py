from django.urls import path
from .views import SignupView, LoginView, UserOperationsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserOperationsView.as_view(), name='user-operations')
]