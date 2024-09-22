from django.db import models

# Create your models here.

class Companies(models.Model):
    corporate_reason = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    contact = models.CharField(max_length=20)
