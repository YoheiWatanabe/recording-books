# Create your views here.
from django.db.models import OuterRef, Subquery, Count
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.books.serializer import CommentSerializer
from backend.books.models.comment import Comment
from backend.books.serializer import BookSerializer
from backend.books.models.book import BookId

from backend.books.serializer import BookIdSerializer

class BookIdViewSet(viewsets.ModelViewSet):
    """BookId view set"""
    permission_classes = [permissions.AllowAny]
    serializer_class = BookIdSerializer
    queryset = BookId.objects.all()


class BookCreate(APIView):
    """Book view"""
    
    def post(self, request, format=None):
        """Create a new book"""
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentList(generics.ListAPIView):
    """Comment view"""
    permission_classes = []
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        """Get query set"""
        subquery = Comment.objects.filter(reply_to=OuterRef('id')).values('reply_to').annotate(count=Count('reply_to')).values('count')
        return Comment.objects.annotate(number_of_replies=Subquery(subquery))
