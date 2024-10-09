from django.shortcuts import render
from .models import Account
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass
# Create your views here.
