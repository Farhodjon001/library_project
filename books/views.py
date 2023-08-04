from django.shortcuts import render
from .models import Book
from .serializers import BookSerializers
from rest_framework import generics

# Create your views here.
class BookListApi(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializers