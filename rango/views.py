from django.http import HttpResponse
from django.shortcuts import render

from rango.models import Category, Page


def index(request):
    categories = Category.objects.order_by('-views')
    pages = Page.objects.order_by('-views')
    return render(request, 'rango/index.html',
                  {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
                   'categories': categories[:5],
                   'pages': pages[:5]})


def about(request):
    return render(request, 'rango/about.html')


def admin(request):
    return render(request, 'rango/admin.html')


def page(request):
    return render(request, 'rango/page.html')


def show_category(request, category_name_slug):
    # print('category_name_slug:', category_name_slug)
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Exception as e:
        category = None

    pages = Page.objects.filter(category=category)
    return render(request, 'rango/category.html', {'category': category, 'pages': pages})
