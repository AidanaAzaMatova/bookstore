from django.db import models

class BookShop(models.Model):
    name_book = models.CharField(max_length=255)
    author_book = models.CharField(max_length=255)
    genre_book = models.CharField(max_length=255)
    publish_year = models.CharField(max_length=255)


