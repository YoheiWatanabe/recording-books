from django.db import models

# Create your models here.

class Language(models.Model):
    """Language model"""
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}, {self.code}'

class Currency(models.Model):
    """Currency model"""
    # cf. currency codes: https://www.iban.jp/currency-codes
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    number = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name
