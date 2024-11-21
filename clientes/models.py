from django.db import models

# Create your models here.
class Companies(models.Model):
    cnpj = models.CharField(max_length=14, primary_key=True)

    corporate_reason = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    contact = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    cell = models.CharField(max_length=11, blank=False)

    class Meta:
        ordering = ['corporate_reason']

    def __str__(self):
        return self.corporate_reason