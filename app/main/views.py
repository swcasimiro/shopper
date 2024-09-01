from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import logging
from products.views import Category

logger = logging.getLogger('file')  # Создаем логгирование действий.

category = Category.objects.all()   # Запрос на создание категорий.


def contact(request):   # Создаем контактную форму и выводим index.html
    logger.info('index.html')   # Логгируем данные с этой функции в наш файл.
    if request.method == 'POST':    # Поведение функции при получение POST-запроса
        form = ContactForm(request.POST)    # Подключаем ранее созданную форму.
        if form.is_valid():     # Проверяем на валидность.
            subject = "Пробное сообщение"
            body = {
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')

    form = ContactForm()    # Отработка GET-запроса.
    context = {
        'form': form,
        'category': category,
    }
    return render(request, "main/index.html", context)



