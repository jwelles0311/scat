from django import forms
from . import models


class ClientesFrom(forms.ModelForm):

    class Meta:
        model = models.Companies
        fields = '__all__'
        widgets = {
            'cnpj': forms.TextInput(attrs={"class": "form-control", "style": "width: 20%; height: 40px; margin-bottom: 10px;"}),
            'corporate_reason': forms.TextInput(attrs={"class": "form-control", "style": "width: 40%; height: 40px; margin-bottom: 10px;"}),

            'address': forms.TextInput(attrs={"class": "form-control", "style": "width: 40%; height: 40px; margin-bottom: 10px;"}),
            'number': forms.TextInput(attrs={"class": "form-control", "style": "width: 10%; height: 40px; margin-bottom: 10px;"}),
            'bairro': forms.TextInput(attrs={"class": "form-control", "style": "width: 30%; height: 40px; margin-bottom: 10px;"}),
            #           'uf': forms.ChoiceWidget(attrs={"class": "form-control", "style": "width: 5%; height: 40px; margin-bottom: 10px;"}),
            'contact': forms.TextInput(attrs={"class": "form-control", "style": "width: 40%; height: 40px; margin-bottom: 10px;"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "style": "width: 40%; height: 40px; margin-bottom: 10px;"}),
            'cell': forms.TextInput(attrs={"class": "form-control", "placeholder": "( )___._____",  "style": "width: 40%; height: 40px; margin-bottom: 10px;"}),
        }
        labels = {
            'cnpj': 'CNPJ',
            'corporate_reason': 'Cliente',
            'address': 'Endereço',
            'number': 'Número',
            'bairro': 'Bairro',
            'uf': 'UF',
            'contact': 'Contato',
            'phone': 'Telefone',
            'cell': 'Celular'



        }
