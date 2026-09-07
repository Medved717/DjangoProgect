from multiprocessing.reduction import register

from django.contrib import admin
from library.models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'publication_date', 'author')
    list_filter = ('author',)
    search_fields = ('title',)

