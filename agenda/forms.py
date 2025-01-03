# forms.py
from django import forms
from .models import WorkingDays
# from .models import Scheduling


class WorkingDaysForm(forms.ModelForm):
    class Meta:
        model = WorkingDays
        fields = ['technician', 'customer',
                  'service', 'date_start', 'date_finish', 'is_working']

        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date_start'}),
            'date_finish': forms.DateInput(attrs={'type': 'date_finish'}),
        }
        labels = {
            'technician': 'Tecnico',
            'customer': 'Cliente',
            'service': 'Serviço',
            'date_start': 'Data Inicial',
            'date_finish': 'Data Final',
            'is_working': 'Status',

        }

        def clean(self):
            cleaned_data = super().clean()
            technician = cleaned_data.get('technician')
            date_start = cleaned_data.get('date_start')

            # Verificar se já existe um agendamento para o técnico na data
            if WorkingDays.objects.filter(technician=technician, date_start=date_start).exists():
                raise forms.ValidationError(
                    f"O técnico {
                        technician} já possui um agendamento para o dia {date_start}."
                )
            return cleaned_data


'''class SchedulingForm(forms.ModelForm):
    class Meta:
        model = Scheduling
        fields = ['observation', 'customer', 'technic',
                  'servic', 'date_start', 'date_finish']
        widgets = {
            'date_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_finish': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
'''
