# Serializer
from rest_framework import serializers
from backend.books.models.store import Store
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


class StoreSerializer(serializers.ModelSerializer):
    """Store serializer"""

    class Meta:
        """Meta"""
        model = Store
        fields = '__all__'


class StoreQuerySerializer(serializers.ModelSerializer):
    """Store query serializer"""

    class Meta:
        """Meta"""
        model = Store
        fields = ['store-name']
        extra_kwargs = {
            'store-name': {
                'source': 'store_name'
            }
        }
