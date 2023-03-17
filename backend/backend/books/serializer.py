# Serializer
from rest_framework import serializers
from backend.books.models.comment import Comment
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


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer"""

    class Meta:
        """Meta"""
        model = Comment
        fields = '__all__'
    
    def to_representation(self, instance):
        """Representation"""
        response = super().to_representation(instance)
        response['reply_count'] = instance.number_of_replies if instance.number_of_replies else 0
        return response
