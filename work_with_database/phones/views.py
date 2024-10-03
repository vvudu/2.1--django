from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_option = request.GET.get('sort', 'name')  # Получаем параметр сортировки из URL

    if sort_option == 'min_price':
        phones = Phone.objects.order_by('price')  # Сортировка по возрастанию цены
    elif sort_option == 'max_price':
        phones = Phone.objects.order_by('-price')  # Сортировка по убыванию цены
    else:
        phones = Phone.objects.order_by('name')  # Сортировка по имени (алфавитный порядок)

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
