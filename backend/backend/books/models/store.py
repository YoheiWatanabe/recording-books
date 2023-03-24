from django.db import models


class Store(models.Model):
    """Store model"""
    store_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)