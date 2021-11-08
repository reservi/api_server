from django.db import models
from .country import Country
from .sex import Sex

class User(models.Model):
    username = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=30, blank=False)
    secondname = models.CharField(max_length=30, blank=False)
    surename = models.CharField(max_length=50, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    street = models.CharField(max_length=50, blank=False)
    postal_code = models.CharField(max_length=15, blank=False)
    birth_date = models.DateField()
    
    class Meta:
        app_label = 'auth'