from django import forms
from . import models


class ServicosForm(forms.ModelForm):

    class Meta:
        model = models.Services
        fields = '__all__'
        widgets = {

            'service': forms.TextInput(attrs={"class": "form-control", "style": "width: 40%; height: 40px; margin-bottom: 10px;"}),


        }
        labels = {
            'service': 'Servico',

        }
