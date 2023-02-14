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
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    isbn = models.CharField(max_length=17, blank=True) 
    asin = models.CharField(max_length=10, blank=True, null=True)
    published_at = models.DateField()
    purchase_date = models.DateField(blank=True, null=True)
    finished_reading = models.BooleanField(blank=True, default=False)
    review = models.TextField(blank=True)
