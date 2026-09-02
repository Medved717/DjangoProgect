from django.shortcuts import render
from django.http import HttpResponse

def about(requests):
    return render(requests, 'students/about.html')


def contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        return HttpResponse(f'Спасибо, {name}, Ваши данные приняты! А это сообщение {message}.')
    else:
        return render(requests, 'students/contact.html')