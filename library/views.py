from django.shortcuts import render
from library.models import Book, Author


def present_book(requests):
    book = Book.objects.get(title='Преступление и наказание')
    context = {'book': book}
    return render(requests, 'library/book.html', context=context)
