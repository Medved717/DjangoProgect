from django import forms
from .models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'email', 'year', 'enrollment_date']
