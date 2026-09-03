from django.db import models

class Author(models.Model):

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата Рождения')

    class Meta:

        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name']

class Book(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название книги')
    publication_date = models.DateField(verbose_name='Дата публикации книги')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class META:

        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']
