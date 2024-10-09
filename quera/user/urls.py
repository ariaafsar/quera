from django.urls import path
from .views import Login , Refresh , Signup

urlptterns = [
    path('login/', Login.as_view(), name='login'),
    path('refresh/', Refresh.as_view(), name='refresh'),
    path('signup/', Signup.as_view(), name='signup'),
]