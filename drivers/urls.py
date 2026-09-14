from django.urls import path
from . import views

app_name='drivers'


urlpatterns = [
    path('drivers_list/', views.DriverListView.as_view(), name='drivers_list'),
    path('drivers_form/', views.DriverCreateView.as_view(), name='drivers_form'),
]
