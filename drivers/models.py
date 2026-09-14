from django.db import models

class Driver(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    document = models.CharField(max_length=100, verbose_name='Документ', blank=True)
    phone = models.CharField(max_length=11, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ('last_name', 'first_name', 'patronymic')

    def __str__(self):
        return f'{self.first_name} {self.patronymic} {self.last_name}'



