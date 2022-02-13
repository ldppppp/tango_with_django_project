from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import ImageFile
from django.db.models.fields.related import OneToOneField
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    views = models.IntegerField(default=1)
    likes = models.IntegerField(default=1)
    slug = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField(max_length=128)
    views = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.fields.related.OneToOneField(User, on_delete=models.CASCADE, default=None)
    website = models.fields.URLField(default='')
    picture = models.fields.files.ImageField(default='')


