from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Category, Page
from .forms import CategoryForm, PageForm


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


def add_category(request):
    form = CategoryForm(request.POST)
    instance = None
    if form.is_valid():
        instance = form.save()

    return render(request, 'rango/add_category.html', {'form': form, 'instance': instance})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        return redirect(reverse('rango:index'))

    p = Page.objects.create(category=category)
    form = PageForm(request.POST, instance=p)

    if form.is_valid():
        form.save()

    return render(request, 'rango/add_page.html', {'form': form, 'category_name_slug': category_name_slug})
