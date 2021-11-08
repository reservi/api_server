from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=50, blank=False)
    country_short_name = models.CharField(max_length=4, blank=False)
    country_img_url = models.CharField(max_length=120, blank=False)

    class Meta:
        app_label = 'src.models.country'

    def __str__(self):
        return self.user.username