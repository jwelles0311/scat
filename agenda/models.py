from django.db import models
from clientes.models import Companies
from tecnicos.models import Technicians
from servicos.models import Services

# Create your models here.
class Scheduling(models.Model):
    observation = models.CharField(max_length=150)
    customer = models.ForeignKey(Companies, on_delete=models.PROTECT)
    technic = models.ForeignKey(Technicians, on_delete=models.PROTECT)
    servic = models.ForeignKey(Services, on_delete=models.PROTECT)
    date_start = models.DateField()
    date_finish = models.DateField()

    class Meta:
        ordering = ['date_start']

    def __str__(self):
        return self.customer