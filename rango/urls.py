from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('show_category/<category_name_slug>/', views.show_category, name='show_category'),
    path('admin/', admin.site.urls),
]
