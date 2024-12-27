from django import forms
from . import models


class TecnicosForm(forms.ModelForm):

    class Meta:
        model = models.Technicians
        fields = '__all__'
        widgets = {

            'name': forms.TextInput(attrs={"class": "form-control", "style": "width: 40%; height: 40px; margin-bottom: 10px;"}),


        }
        labels = {
            'name': 'Nome',

        }
