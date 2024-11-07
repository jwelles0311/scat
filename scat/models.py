from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Companies(models.Model):
    cnpj = models.CharField(max_length=14, primary_key=True, validators=[RegexValidator(
        regex=r'^\d{14}$', message='O CNPJ deve conter 14 dígitos numéricos.')], verbose_name="CNPJ")

    corporate_reason = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=50, blank=False, null=True)
    number = models.CharField(max_length=10, blank=False, null=True)
    contact = models.CharField(max_length=30, blank=False, null=True)
    phone = models.CharField(max_length=10, blank=False, null=True)
    cell = models.CharField(max_length=11)


class Technicians(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)


class Services(models.Model):
    service = models.CharField(max_length=50, blank=False, null=True)


class Scheduling(models.Model):
    observation = models.CharField(max_length=150)
    customer = models.ForeignKey(Companies, on_delete=models.PROTECT)
    technic = models.ForeignKey(Technicians, on_delete=models.PROTECT)
    servic = models.ForeignKey(Services, on_delete=models.PROTECT)
    date_start = models.DateField()
    date_finish = models.DateField()
