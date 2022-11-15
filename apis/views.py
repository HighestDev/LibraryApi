from django.shortcuts import render
from books.models import Book
from rest_framework import generics
from apis.serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    
