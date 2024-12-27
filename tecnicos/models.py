from django.db import models

# Create your models here.


class Technicians(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Converte o texto para maiúsculas
        self.name = self.name.title()
        # Converte a primeira Letra para maiúscula
        super().save(*args, **kwargs)
