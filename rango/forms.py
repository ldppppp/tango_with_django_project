import django.forms
from django.forms import ModelForm

from .models import Category, Page


class CategoryForm(ModelForm):

    slug = django.forms.CharField(required=False)

    class Meta:
        model = Category
        fields = ['name', 'views', 'likes', 'slug']


class PageForm(ModelForm):
    title = django.forms.CharField(required=False)
    url = django.forms.URLField(required=False)
    views = django.forms.IntegerField(required=False)

    class Meta:
        model = Page
        fields = ['title', 'url', 'views']
