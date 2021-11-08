from django.db import models

class Sex(models.Model):
    sex_shortcut = models.CharField(max_length=4, blank=False)
    sex_full = models.CharField(max_length=40, blank=False)

    class Meta:
        app_label = 'src.models.sex'

    def __str__(self):
        return self.user.username