from .models import Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Author
        fields='__all__'
    books= BookSerializer(read_only=True,many=True)


