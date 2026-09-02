from django.urls import path
from . import views

app_name = 'example'

urlpatterns = [
    path('example_contact/', views.example_contact, name='example_contact')
]