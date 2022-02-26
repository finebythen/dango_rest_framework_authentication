from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)


admin.site.site_header = "Django Rest Framework - Tutorial"
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)