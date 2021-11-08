from django.db import models
# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=50, blank=False)
    country_short_name = models.CharField(max_length=4, blank=False)
    country_img_url = models.CharField(max_length=120, blank=False)

    def __str__(self):
        return self.country_short_name

class Sex(models.Model):
    sex_shortcut = models.CharField(max_length=4, blank=False)
    sex_full = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return self.sex_shortcut



class UserModel(models.Model):
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

    def __str__(self):
        return self.username
