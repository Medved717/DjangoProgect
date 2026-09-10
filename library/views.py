from django.shortcuts import render
from library.models import Book, Author


def books_list(requests):
    books = Book.objects.all()
    context = {'books': books}
    return render(requests, 'library/books_list.html', context=context)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book': book}
    return render(request, 'library/book_detail.html', context=context)


