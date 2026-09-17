from django.urls import reverse_lazy
from library.forms import BookForm, AuthorForm
from library.models import Book, Author
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from students.models import Students


class BooksListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'


class BooksCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books_form.html'
    success_url = reverse_lazy('library:books_list')


class BooksUpdateView(UpdateView):
    model = Book
    template_name = 'library/books_form.html'
    form_class = BookForm
    success_url = reverse_lazy('library:books_list')


class BooksDeleteView(DeleteView):
    model = Book
    template_name = 'library/books_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')

class BooksDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/books_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'library/author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('library:author_list')


class AuthorListView(ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    context_object_name = 'author'
    success_url = reverse_lazy('library:author_list')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author'

