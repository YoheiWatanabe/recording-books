from django.db import models

from backend.books.models.category import Category
from backend.books.models.master import Language

from backend.books.models.master import Currency

# Create your models here.

class Price(models.Model):
    """Price model"""
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self) -> str:
        price = int(self.price) if self.unit.code == 'JPY' else self.price
        return f'{price}{self.unit}'


class Review(models.Model):
    """Review model"""
    rating = models.IntegerField()
    text = models.TextField()


class Author(models.Model):
    """Author model"""
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class BookId(models.Model):
    """A model which deals with special book ids: ISBN and ASIN"""
    isbn10 = models.CharField(max_length=13)
    isbn13 = models.CharField(max_length=17)
    asin = models.CharField(max_length=10)


class Book(models.Model):
    """Book model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book_id = models.ForeignKey(to=BookId, on_delete=models.PROTECT, related_name='book_id')
    authors = models.ManyToManyField(to=Author, related_name='authors')
    title = models.TextField(max_length=500)
    price = models.ForeignKey(to=Price, on_delete=models.DO_NOTHING)
    language = models.ForeignKey(to=Language, on_delete=models.DO_NOTHING, related_name='language')
    publisher = models.CharField(max_length=50)
    published_at = models.DateField()
    purchase_date = models.DateField(null=True, default=None)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='category_id')
    review = models.ForeignKey(to=Review, null=True, default=None, on_delete=models.SET_DEFAULT, related_name='review')
    finished_reading = models.BooleanField()
    is_wish = models.BooleanField()
    is_deleted = models.BooleanField()
