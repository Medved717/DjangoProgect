from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .forms import StudentsForm
from .models import Students


class StudentsCreateView(CreateView):
    model = Students
    form_class = StudentsForm
    template_name = 'students/students_form.html'
    success_url = reverse_lazy('students:students_list')


class StudentsUpdateView(UpdateView):
    model = Students
    form_class = StudentsForm
    context_object_name = 'students'
    template_name = 'students/students_form.html'
    success_url = reverse_lazy('students:students_list')


class StudentsListView(ListView):
    model = Students
    context_object_name = 'students'
    template_name = 'students/students_list.html'


class StudentsDetailView(DetailView):
    model = Students
    context_object_name = 'students'
    template_name = 'students/students_detail.html'
