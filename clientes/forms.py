from django import forms
from . import models

class ClientesFrom(forms.ModelForm):

    class Meta:
        model = models.Companies
        fields = ['corporate_reason', 'address', 'number']
