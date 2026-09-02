from django.shortcuts import render
from django.http import HttpResponse

def example_contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        password = requests.POST.get('password')
        return HttpResponse(f'Мы получили Ваш запрос, {name}!')
    return render(requests, 'example/example_contact.html/')


