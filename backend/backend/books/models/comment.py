"""Comment Model"""

from django.db import models

class Comment(models.Model):
    """Comment model"""
    text = models.CharField(max_length=2000)
    reply_to = models.ForeignKey(to='self', on_delete=models.DO_NOTHING, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.text