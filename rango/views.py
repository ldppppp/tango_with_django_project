from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'rango/index.html', {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'})


def about(request):

    return render(request, 'rango/about.html')