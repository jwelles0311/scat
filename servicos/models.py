from django.db import models

# Create your models here.


class Services(models.Model):
    service = models.CharField(max_length=50)

    class Meta:
        ordering = ['service']

    def __str__(self):
        return self.service

    def save(self, *args, **kwargs):

        # Converte a primeira Letra para maiúscula
        self.service = self.service.title()
        super().save(*args, **kwargs)
