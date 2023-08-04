from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        modul=Book
        fields=['title','subtitle','author','isbn','price',]

