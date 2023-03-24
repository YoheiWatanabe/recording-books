from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.books.views import StoreList
from backend.books.views import BookCreate

from backend.books.views import BookIdViewSet

router = DefaultRouter()
router.register('book-id', BookIdViewSet, basename='book-id')

urlpatterns = [
    path('books/', BookCreate.as_view()),
    path('stores/', StoreList.as_view()),
    path('', include(router.urls)),
]
