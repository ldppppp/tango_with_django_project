from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    views = models.IntegerField(default=1)
    likes = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    views = models.IntegerField(default=1)

    def __str__(self):
        return self.title
