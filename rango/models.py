from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128)
    views = models.IntegerField(default=1)
    likes = models.IntegerField(default=1)
    slug = models.SlugField(max_length=250, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    views = models.IntegerField(default=1)

    def __str__(self):
        return self.title
