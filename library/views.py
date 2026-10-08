from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import cache_page

from library.forms import BookForm, AuthorForm
from library.models import Book, Author
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from library.services import ReviewService


class BooksListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'
    permission_required = 'library.view_book'


class ReviewBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if not request.user.has_perm('library.can_review_book'):
            return HttpResponseForbidden('У Вас нет права для рецензирования книги.')

        book.review = request.POST.get('review')
        book.save()
        return redirect('library:books_detail', pk=pk)


class RecomendBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if request.user.has_perm('library.can_recommend_book'):
            return HttpResponseForbidden('У Вас нет права для рекомендации книги.')

        book.recommend = True
        book.save()
        return redirect('library:book_detail', pk=pk)


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


@method_decorator(cache_page(60 * 15), name='dispatch')
class BooksDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/books_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['author_books_count'] = Book.objects.filter(author=self.object.author).count()

        book_id = self.object.id
        context_data['average_rating'] = ReviewService.calculate_average_rating(book_id)
        context_data['is_popular'] = ReviewService.is_popular(book_id)

        return context_data


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
