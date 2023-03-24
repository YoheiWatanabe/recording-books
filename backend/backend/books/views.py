# Create your views here.
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.books.serializer import StoreQuerySerializer, StoreSerializer
from backend.books.models.store import Store
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


class StoreList(generics.ListAPIView):
    """Store list"""
    permission_classes = []
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def list(self, request, *args, **kwargs):
        if not request.query_params:
            return super().list(request, *args, **kwargs)
        query_serializer = StoreQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        store_name = query_serializer.validated_data['store_name']
        queryset = Store.objects.filter(store_name__contains=store_name)
        return Response(data=self.get_serializer(queryset, many=True).data)