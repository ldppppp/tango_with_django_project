import django.forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Category, Page, UserProfile


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


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(ModelForm):
    website = django.forms.URLField(required=False)
    picture = django.forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['website', 'picture']