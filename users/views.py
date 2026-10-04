from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
import secrets
from config.settings import EMAIL_HOST_USER
from .models import CustomUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('library:books_list')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        host = self.request.get_host()
        url = f'http://{host}/users/email_verification/{token}/'
        user.save()
        send_mail(
            subject='Добро пожаловать на наш сервис!',
            message=f'Для подтверждения учетной записи перейдите по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]

        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('students:students_list'))
