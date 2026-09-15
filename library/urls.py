from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('library/books_list/', views.BooksListView.as_view(), name='books_list'),
    path('library/books_form/', views.BooksCreateView.as_view(), name='books_create'),
    path('library/books_form/<int:pk>/', views.BooksUpdateView.as_view(), name='books_update'),
    path('library/books_confirm_delete/<int:pk>/', views.BooksDeleteView.as_view(), name='books_delete'),
    path('library/books_detail/<int:pk>/', views.BooksDetailView.as_view(), name='books_detail'),
]