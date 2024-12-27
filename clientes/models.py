

# Create your models here.


from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


class Companies(models.Model):
    # Lista de estados brasileiros
    class UFChoices(models.TextChoices):
        AC = 'AC', 'Acre'
        AL = 'AL', 'Alagoas'
        AP = 'AP', 'Amapá'
        AM = 'AM', 'Amazonas'
        BA = 'BA', 'Bahia'
        CE = 'CE', 'Ceará'
        DF = 'DF', 'Distrito Federal'
        ES = 'ES', 'Espírito Santo'
        GO = 'GO', 'Goiás'
        MA = 'MA', 'Maranhão'
        MT = 'MT', 'Mato Grosso'
        MS = 'MS', 'Mato Grosso do Sul'
        MG = 'MG', 'Minas Gerais'
        PA = 'PA', 'Pará'
        PB = 'PB', 'Paraíba'
        PR = 'PR', 'Paraná'
        PE = 'PE', 'Pernambuco'
        PI = 'PI', 'Piauí'
        RJ = 'RJ', 'Rio de Janeiro'
        RN = 'RN', 'Rio Grande do Norte'
        RS = 'RS', 'Rio Grande do Sul'
        RO = 'RO', 'Rondônia'
        RR = 'RR', 'Roraima'
        SC = 'SC', 'Santa Catarina'
        SP = 'SP', 'São Paulo'
        SE = 'SE', 'Sergipe'
        TO = 'TO', 'Tocantins'

    cnpj = models.CharField(
        max_length=14,
        primary_key=True,
        unique=True,
        verbose_name="CNPJ"

    )
    corporate_reason = models.CharField(max_length=100, verbose_name="Cliente")
    address = models.CharField(max_length=50, verbose_name="Endereço")
    number = models.CharField(max_length=10, verbose_name="Numero")
    bairro = models.CharField(max_length=30, verbose_name="Bairro")
    uf = models.CharField(
        max_length=2,
        choices=UFChoices.choices,
        default=UFChoices.SP  # Valor padrão: São Paulo
    )
    contact = models.CharField(max_length=30, verbose_name="Contato")
    phone = models.CharField(max_length=10, verbose_name="Tel")
    cell = models.CharField(max_length=11, blank=False, verbose_name="Cel")

    class Meta:
        ordering = ['corporate_reason']

    def __str__(self):
        return self.corporate_reason

    def save(self, *args, **kwargs):
        # Converte o texto para maiúsculas
        self.corporate_reason = self.corporate_reason.upper()
        # Converte a primeira Letra para maiúscula
        self.address = self.address.title()
        self.bairro = self.address.title()
        self.contact = self.address.title()
        super().save(*args, **kwargs)
