from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('present_book/', views.present_book, name='present_book'),]