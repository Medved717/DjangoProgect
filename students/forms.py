from django import forms
from .models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'email', 'year', 'enrollment_date']

        def clean_mail(self):
            email = self.cleaned_data.get('email')
            if not email.endswith('@example.com'):
                raise ValidationError('email должен оканчиваться на @example.com')
            return email



