from django.urls import reverse_lazy
from library.forms import BookForm, AuthorForm
from library.models import Book, Author
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BooksListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'
    permission_required = 'library.view_book'


class BooksCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/books_form.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.add_book'


class BooksUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'library/books_form.html'
    form_class = BookForm
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.change_book'


class BooksDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'library/books_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.delete_book'


class BooksDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/books_detail.html'


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Author
    template_name = 'library/author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('library:author_list')
    permission_required = 'library.add_book'


class AuthorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'
    permission_required = 'library.view_book'


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    context_object_name = 'author'
    success_url = reverse_lazy('library:author_list')
    permission_required = 'library.change_book'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author'
