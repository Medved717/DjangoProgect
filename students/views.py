from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def about(requests):
    return render(requests, 'students/about.html')


def contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        return HttpResponse(f'Спасибо, {name}, Ваши данные приняты! А это сообщение {message}.')
    else:
        return render(requests, 'students/contact.html')

def index(requests):
    student = Student.objects.get(id='1')
    context = {
        'student_name': f'{student.first_name} {student.last_name}',
        'student_year': student.get_year_display()
    }
    return render(requests, 'students/index.html', context=context)


def student_detail(requests):
    student = Student.objects.get(id='1')
    context = {
        'student': student
    }

    return render(requests, 'students/student_detail.html', context=context)


def student_list(requests):
    students = Student.objects.all()
    context = {'students': students}
    return render(requests, 'students/student_list.html', context=context)