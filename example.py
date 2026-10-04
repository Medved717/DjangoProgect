
from django.template.defaulttags import URLNode


def get_context_data(self, **kwargs):
    context_data = super().get_context_data(**kwargs)
    CategoryFormset = inlineformset_factory(Category, Product, form=ProductForm, extra=1)
    if self.request.method == 'POST':
        context_data['formset'] = CategoryFormset(self.request.POST, instance=self.object)
    else:
        context_data['formset'] = CategoryFormset(instance=self.object)
    return context_data


def form_valid(self, form):
    context_data = self.get_context_data()
    formset = context_data['formset']
    if formset.is_valid():
        self.object = form.save()
        formset.instance = self.object
        formset.save()
    return super().form_valid(form)


from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    number_phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


from django.forms import inlineformset_factory


def get_context_data(self, **kwargs):
    context_data = super().get_context_data(**kwargs)
    CategoryFormset = inlineformset_factory(Category, Product, form=ProductForm, extra=1)
    if self.request.method == 'POST':
        context_data['formset'] = CategoryFormset(self.request.POST, instance=self.object)
    else:
        context_data['formset'] = CategoryFormset(instance=self.object)
    return context_data


def form_valid(self, form):
    context_data = self.get_context_data()
    formset = context_data['formset']
    if formset.is_valid():
        self.object = form.save()
        formset.instance = self.object
        formset.save()
    return super().form_valid(form)


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import ValidationError


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False,
                                   help_text='Введите необязательно поле номера телефона.')
    username = forms.CharField(max_length=50, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise ValidationError
        return phone_number




# Создание контроллера, валидации и функции для отправки привтественного письма.
# Дополнительно нужно создать поле token в модели пользователя.


class RegisterView(CreateView):
    form_class = UserRegister
    template_name = 'users/register_users.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        user.token = secrets.token_hex(16)
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{user.token}/'
        send_mail(
            subject='Добро пожоловать на наш сервис!',
            message=f'Для подтверждения аккаунта перейдите по следующей ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


from django.urls import reverse_lazy
from .models import User
import secrets
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('library:books_list')

    def form_valid(self, form):
        user = form
        user.is_active = False
        user.token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f'http://{host}/users/email_register/{user.token}/'
        user.save()
        send_mail(
            subject='Добро пожаловать!',
            message=f'Перейди по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('library:books_list'))


