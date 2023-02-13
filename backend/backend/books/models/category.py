"""Category model"""
from django.db import models


class Category(models.Model):
    parent_id = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.PROTECT, related_name='parent_category')
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=50)
