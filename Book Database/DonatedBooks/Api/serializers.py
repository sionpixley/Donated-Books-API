from rest_framework import serializers
from Api.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("Id", "Title", "AuthorFirstName", "AuthorLastName", "Price", "Quantity")
