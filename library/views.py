# from django.shortcuts import render
from django.urls import reverse_lazy

from library.models import Book, Author
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView


class BooksListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'


class BooksCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/books_form.html'
    success_url = reverse_lazy('library:books_list')


class BooksUpdateView(UpdateView):
    model = Book
    template_name = 'library/books_form.html'
    fields = ['title', 'publication_date', 'author']
    success_url = reverse_lazy('library:books_list')


class BooksDeleteView(DeleteView):
    model = Book
    template_name = 'library/books_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')

class BooksDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/books_detail.html'
