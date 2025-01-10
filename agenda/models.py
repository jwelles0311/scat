
from django.db import models
from clientes.models import Companies
from tecnicos.models import Technicians
from servicos.models import Services


class WorkingDays(models.Model):
    STATUS_CHOICES = [
        ('AGENDADO', 'Agendado'),
        ('ANDAMENTO', 'Em andamento'),
        ('CONCLUIDO', 'Concluído'),
    ]

    technician = models.ForeignKey(Technicians, on_delete=models.CASCADE)
    customer = models.ForeignKey(Companies, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_finish = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='AGENDADO'
    )
    result_description = models.TextField(
        blank=True,
        null=True,

    )

    class Meta:
        unique_together = ('technician', 'date_start')
        ordering = ['date_start']

    def __str__(self):
        return f"{self.technician} - {self.date_start} - {self.get_status_display()}"
