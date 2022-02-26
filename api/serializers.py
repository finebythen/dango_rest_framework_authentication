from rest_framework import serializers
from app_auth.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
    
    def get_author_first_name(self, obj):
        return obj.author.first_name
    
    def get_author_last_name(self, obj):
        return obj.author.last_name    