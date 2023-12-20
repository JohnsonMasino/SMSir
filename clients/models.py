from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Industry(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.description}"


class Country(models.Model):
    name = models.EmailField(max_length=100)
    code = models.EmailField(max_length=10, default='')

    def __str__(self):
        return f"{self.name} {self.code}"


class Client(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)
    location = models.CharField(max_length=300, default='')
    brand_name = models.CharField(max_length=100, default='')
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.full_name
