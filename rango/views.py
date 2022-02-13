from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CategoryForm, PageForm, UserForm, UserProfileForm
from .models import Category, Page


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
    # return HttpResponse('<p>Models in the Rango application</p> <p>Categories</p> <p>Pages</p>')
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
    # todo: Comment the following if when testing the test_chapter7.py.
    if not request.user.is_authenticated:
        return redirect(reverse('rango:login'))

    form = CategoryForm(request.POST)
    instance = None
    if form.is_valid():
        instance = form.save()

    return render(request, 'rango/add_category.html', {'form': form, 'instance': instance})


def add_page(request, category_name_slug):
    # todo: Comment the following if when testing the test_chapter7.py.
    if not request.user.is_authenticated:
        return redirect(reverse('rango:login'))

    try:
        category = Category.objects.get(slug=category_name_slug)
    except:
        return redirect(reverse('rango:index'))

    p = Page.objects.create(category=category)
    form = PageForm(request.POST, instance=p)

    if form.is_valid():
        form.save()

    return render(request, 'rango/add_page.html', {'form': form, 'category_name_slug': category_name_slug})


def userprofile(request):
    return HttpResponse()


def register(request):
    if request.method == 'POST':  # Post submit
        try:
            user_form = UserForm({'username': request.POST['username'], 'password': request.POST['password'],
                                  'email': request.POST['email']})
            user_profile_form = UserProfileForm(
                {'website': request.POST['website'], 'picture': request.POST['picture']})

            if user_form.is_valid() and user_profile_form.is_valid():
                user = user_form.save()
                user.set_password(request.POST['password'])
                user.save()

                user_profile = user_profile_form.save(commit=False)
                user_profile.user = user
                user_profile.save()

            return render(request, 'rango/register.html',
                          {'user_form': user_form, 'userprofile_form': user_profile_form, 'status': 'T'})
        except:

            return render(request, 'rango/register.html', {'status': 'F'})
    else:  # normal visit
        user_form = UserForm()
        user_profile_form = UserProfileForm()
        return render(request, 'rango/register.html',
                      {'user_form': user_form, 'userprofile_form': user_profile_form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)

        return redirect(reverse('rango:index'))

    return render(request, 'rango/login.html')


def restricted(request):
    if not request.user.is_authenticated:
        return redirect(reverse('rango:login'))

    return render(request, 'rango/restricted.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('rango:index'))