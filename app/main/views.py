from django.shortcuts import render


def index(request):

    context = {'title': 'Home - Главная',
               'content': 'Добро пожаловать в магазин мебели HOME',
               }
    return render(request, 'main/index.html', context)


def about(request):
    context = {'title': 'Home - О нас',
               'content': 'О нас',
               }
    return render(request, 'main/about.html', context)


def delivery_payment(request):
    context = {'title': 'Home - Доставка и оплата',
               'content': 'Доставка и оплата',
               }
    return render(request, 'main/delivyry_payment.html', context)


def contacts(request):
    context = {'title': 'Home - Контакты',
               'content': 'Контакты',
               }
    return render(request, 'main/contacts.html', context)