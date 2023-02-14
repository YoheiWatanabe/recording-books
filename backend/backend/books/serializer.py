# Serializer
from rest_framework import serializers
from backend.books.models.book import Book

from backend.books.models.book import BookId

class BookIdSerializer(serializers.ModelSerializer):
    """BookId serializer"""

    class Meta:
        """Meta"""
        model = BookId
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """Book serializer"""
    
    class Meta:
        """Meta"""
        model = Book
        fields = '__all__'
