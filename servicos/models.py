from django.db import models

# Create your models here.

class Services(models.Model):
    service = models.CharField(max_length=50)

    class Meta:
        ordering = ['service']

    def __str__(self):
        return self.service