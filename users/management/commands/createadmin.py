from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.obgects.create(
            email='admin@mail.ru',
            phone_number='89999999999',
            first_name='Ivan',
            last_name='Ivanov'
        )

        user.set_password = '1234'
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return self.stdout.write(
            self.style.SUCCSSES(f'Поздравляю, Вы зарегистрировали пользователя с идентификатором {user.email}'))
