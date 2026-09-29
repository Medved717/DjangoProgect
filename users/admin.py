from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Поля, отображаемые в списке пользователей
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')

    # Поля для формы редактирования
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('phone_number', 'avatar')}),
    )

    # Поля для формы создания
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {'fields': ('email', 'phone_number', 'avatar')}),
    )

    # Поиск по email и username
    search_fields = ('email', 'username', 'first_name', 'last_name')

    # Сортировка
    ordering = ('email',)