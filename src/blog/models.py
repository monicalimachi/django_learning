from datetime import date, datetime
from django.db import models

# Create your models here.
class Article(models.Model):
    title       =models.CharField(max_length=120)
    content     =models.TextField(default='This is test')
    date        =models.DateTimeField(auto_now_add=True, blank=True)
    active      =models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)