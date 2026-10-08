from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .forms import StudentsForm
from .models import Students
from django.shortcuts import get_object_or_404, redirect
from django.core.cache import cache
from .services import StudentsService


class PromoteStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Students, id=student_id)

        if not request.user.has_perm('Student.can_promote_student'):
            return HttpResponseForbidden('У Вас нет прав для перевода студента.')

        student.year = next_year(student.year)
        student.save()
        return redirect('students:students_list')


class ExpelStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Students, id=student_id)

        if not request.user.has_perm('Student.can_expel_student'):
            return HttpResponseForbidden('У Вас нет прав для исключения студента.')

        student.delete()
        return redirect('students:students_list')


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

    def get_queryset(self):
        if not self.request.user.has_perm('students.view_student'):
            return Students.objects.none()
        return Students.objects.all()


class StudentsDetailView(DetailView):
    model = Students
    context_object_name = 'students'
    template_name = 'students/students_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student_id = self.objects.id

        context['full_name'] = StudentsService.get_full_name(student_id)
        context['average_grade'] = StudentsService.calculate_average_score(student_id)
        context['has_passed'] = StudentsService.has_passed(student_id)

        return context

def my_view(request, pk):
    data = cache.get(f'product_{pk}')

    if not data:
        data = get_object_or_404(Product, pk=pk)
        cache.set(f'product_{pk}', data, 60 * 15)

    return render(request, 'catalog/product_detail.html', {'product': data})


