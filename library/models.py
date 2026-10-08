from django.db import models
from django.db.models import TextField


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата Рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name']


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    publication_date = models.DateField(verbose_name='Дата публикации книги')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    review = models.TextField(null=True, blank=True)
    recommend = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']
        permissions = [
            ('can_review_book', 'can review book'),
            ('can_recommend_book', 'can recommend book')
        ]


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review for {self.book.title}'