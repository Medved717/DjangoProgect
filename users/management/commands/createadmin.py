from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            username='admin',
            first_name='Ivan',
            last_name='Ivanov',
            email='admin@mail.ru',
            phone_number='89999999999'
        )

        user.set_password('1234')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return self.stdout.write(self.style.SUCCESS(f'Пользователь с логином {user.email} создан.'))