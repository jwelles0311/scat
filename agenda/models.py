
# models.py
from django.db import models
from clientes.models import Companies
from tecnicos.models import Technicians
from servicos.models import Services


'''class Scheduling(models.Model):
    observation = models.CharField(max_length=150)
    customer = models.ForeignKey(Companies, on_delete=models.PROTECT)
    technic = models.ForeignKey(Technicians, on_delete=models.PROTECT)
    servic = models.ForeignKey(Services, on_delete=models.PROTECT)
    date_start = models.DateField()
    date_finish = models.DateField()

    class Meta:
        ordering = ['date_start']

    def __str__(self):
        return f"{self.customer} - {self.technic}"  # Ajuste no retorno
'''


class WorkingDays(models.Model):
    technician = models.ForeignKey(Technicians, on_delete=models.CASCADE)
    customer = models.ForeignKey(Companies, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
#    date = models.DateField()
    date_start = models.DateField()
    date_finish = models.DateField()
  #  True = Trabalhando, False = Livre,
    is_working = models.BooleanField(default=False)

    class Meta:
        unique_together = ('technician', 'date_start')
        ordering = ['date_start']

    def __str__(self):
        status = "Trabalhando" if self.is_working else "Livre"
        return f"{self.technician} - {self.date_start}: {status}"
