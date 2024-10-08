from django.shortcuts import render
from .models import Class 
from .serializers import CreateClassSerializer
from rest_framework import generics , status
from rest_framework.response import Response

class CreateClass(generics.CreateAPIView):
    serializer_class = CreateClassSerializer
    queryset = Class.objects.all()
    def CreateClass(self , request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
