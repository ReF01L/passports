from django.db import models


def upload_path(instance, name):
    return f'user_{instance.name}/{name}'


class Barsa(models.Model):
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    user_id = models.CharField(max_length=32)
    nat = models.CharField(max_length=64)
    gunlic = models.CharField(max_length=32, blank=True, default='нет')
    crime = models.CharField(max_length=32, blank=True, default='нет')
    image = models.ImageField(upload_to=upload_path, blank=True, null=True, default=None)


class Profile(models.Model):
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
