# forms.py
from django import forms
from .models import WorkingDays


class WorkingDaysForm(forms.ModelForm):
    class Meta:
        model = WorkingDays
        fields = [
            'technician',
            'customer',
            'service',
            'date_start',
            'date_finish',
            'status',
            'result_description'
        ]

        widgets = {

            'status': forms.Select(choices=WorkingDays.STATUS_CHOICES),
            'result_description': forms.Textarea(attrs={'rows': 3, }),
            'date_start': forms.DateInput(attrs={'date': "d/m/Y"}),
            'date_finish': forms.DateInput(attrs={'date': "d/m/y"}),
        }

        labels = {
            'technician': 'Técnico',
            'customer': 'Cliente',
            'service': 'Serviço',
            'date_start': 'Data Inicial',
            'date_finish': 'Data Final',
            'status': 'Status do Serviço',
            'result_description': 'Descrição do Resultado Final do Serviço',
        }

    def clean(self):
        cleaned_data = super().clean()
        technician = cleaned_data.get('technician')
        date_start = cleaned_data.get('date_start')

        # Verificar se já existe um agendamento para o técnico na data
        if WorkingDays.objects.filter(technician=technician, date_start=date_start).exists():
            raise forms.ValidationError(
                f"O técnico {technician} já possui um agendamento para o dia {
                    date_start}."
            )
        return cleaned_data


class WorkingDaysDayForm(forms.ModelForm):
    class Meta:
        model = WorkingDays
        fields = [
            'technician',
            'customer',
            'service',
            'date_start',
            'date_finish',
            'status',
            'result_description'
        ]

        widgets = {

            'status': forms.Select(choices=WorkingDays.STATUS_CHOICES),
            'result_description': forms.Textarea(attrs={'rows': 3, }),
            'date_start': forms.DateInput(attrs={'date': "d/m/Y"}),
            'date_finish': forms.DateInput(attrs={'date': "d/m/y"}),
        }

        labels = {
            'technician': 'Técnico',
            'customer': 'Cliente',
            'service': 'Serviço',
            'date_start': 'Data Inicial',
            'date_finish': 'Data Final',
            'status': 'Status do Serviço',
            'result_description': 'Descrição do Resultado Final do Serviço',
        }

    def clean(self):
        cleaned_data = super().clean()
        technician = cleaned_data.get('technician')
        date_start = cleaned_data.get('date_start')
