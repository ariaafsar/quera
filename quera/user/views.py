from django.shortcuts import render
from .models import Account
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics , status
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterAccountSerializer
from rest_framework.response import Response


class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

class Signup(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterAccountSerializer
    def create(self , request , *args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Create your views here.
