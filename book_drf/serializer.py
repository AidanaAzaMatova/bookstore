from rest_framework import serializers
from .models import BookShop

class SerializerBookShop(serializers.ModelSerializer):
    class Meta:
        model = BookShop
        fields = (
            'name_book',
            'author_book',
            'genre_book',
            'publish_year'
        )

