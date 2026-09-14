from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Driver
from django.urls import reverse_lazy


class DriverListView(ListView):
    model = Driver
    template_name = 'drivers/drivers_list.html'
    context_object_name = 'drivers'


class DriverCreateView(CreateView):
    model = Driver
    fields = ['last_name', 'first_name', 'patronymic', 'birth_date', 'document', 'phone']
    template_name = 'drivers/drivers_form.html'
    success_url = reverse_lazy('drivers:drivers_list')
