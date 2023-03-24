from django.contrib import admin
from backend.books.models.store import Store
from backend.books.models.book import Book
from backend.books.models.book import BookId
from backend.books.models.book import Author
from backend.books.models.book import Review
from backend.books.models.category import Category
from backend.books.models.book import Price
from backend.books.models.master import Currency

from backend.books.models.master import Language


# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    """Display Language model"""
    model = Language
    list_display = ('id', 'name', 'code')


class CurrencyAdmin(admin.ModelAdmin):
    """Display Currency model"""
    model = Currency
    list_display = ('id', 'name', 'country', 'code', 'number')


class PriceAdmin(admin.ModelAdmin):
    """Display Price model"""
    model = Price
    list_display = ('id', 'price', 'unit')


class CategoryAdmin(admin.ModelAdmin):
    """Display Category model"""
    model = Category
    list_display = ('id', 'parent_id', 'name', 'code')


class ReviewAdmin(admin.ModelAdmin):
    """Display Review model"""
    model = Review
    list_display = ('id', 'rating', 'text')


class AuthorAdmin(admin.ModelAdmin):
    """Display Author model"""
    model = Author
    list_display = ('id', 'first_name', 'last_name')


class BookIdAdmin(admin.ModelAdmin):
    """Display BookId model"""
    model = BookId
    list_display = ('id', 'isbn10', 'isbn13', 'asin')


class BookAdmin(admin.ModelAdmin):
    """Display Book model"""
    model = Book
    list_display = ('id', 'book_id', 'title', 'price',
                    'language', 'publisher', 'published_at', 'purchase_date',
                    'category', 'review', 'finished_reading', 'is_wish', 'is_deleted',
                    )

class StoreAdmin(admin.ModelAdmin):
    """Display Store model"""
    model = Store
    list_display = ('id', 'store_name', 'address')

admin.site.register(Language, LanguageAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookId, BookIdAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Store, StoreAdmin)
