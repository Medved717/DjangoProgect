from django.db import models

class Students(models.Model):
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR = 'fourth'

    YEAR_IN_COLLAGE = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс'),
    ]


    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    year = models.CharField(max_length=6, choices=YEAR_IN_COLLAGE, verbose_name='Курс')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:

        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name']
