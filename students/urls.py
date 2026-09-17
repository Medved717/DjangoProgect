from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('students_form/', views.StudentsCreateView.as_view(), name='students_create'),
    path('students_form/<int:pk>/', views.StudentsUpdateView.as_view(), name='students_update'),
    path('students_list/', views.StudentsListView.as_view(), name='students_list'),
    path('students_detail/<int:pk>/', views.StudentsDetailView.as_view(), name='students_detail'),
]
