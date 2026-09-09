from django.contrib import admin
from .models import Student

@admin.register(Student)
class AdminStudents(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'year']
    list_filter = ('year',)
    search_fields = ['first_name', 'last_name']
