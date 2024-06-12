from django.shortcuts import render
from rest_framework import generics
from .models import CreativeWork
from .serializers import CreativeWorkSerializer

class CreativeWorkListCreate(generics.ListCreateAPIView):
    queryset = CreativeWork.objects.all()
    serializer_class = CreativeWorkSerializer

class CreativeWorkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreativeWork.objects.all()
    serializer_class = CreativeWorkSerializer
