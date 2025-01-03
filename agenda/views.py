# from django.shortcuts import render, redirect
from . import models

from .forms import WorkingDaysForm

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

# from .forms import SchedulingForm
import json


from django.views.generic.list import ListView
from .models import WorkingDays
from django.db.models import Q


from django.views.generic.list import ListView
from .models import WorkingDays
from django.db.models import Q


class WorkingDaysListView(ListView):
    model = WorkingDays
    template_name = 'workingdays_list.html'
    context_object_name = 'workingdays'
    ordering = ['date_start']
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtém os parâmetros do GET
        date_start = self.request.GET.get('date_start')
        date_finish = self.request.GET.get('date_finish')
        technician_id = self.request.GET.get('technician')

        # Filtrar por período de datas
        if date_start and date_finish:
            queryset = queryset.filter(
                Q(date_start__gte=date_start) & Q(date_finish__lte=date_finish)
            )

        # Filtrar por técnico
        if technician_id:
            queryset = queryset.filter(technician__id=technician_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Passa os técnicos para o template
        context['technicians'] = self.model.objects.values(
            'technician__id', 'technician__name').distinct()
        return context


def technician_schedule_view(request):
    # Filtra os agendamentos e status dos dias
 #   schedules = Scheduling.objects.all()
    working_days = WorkingDays.objects.all()

    # Passa os dados para o template
    context = {
        #    'schedules': schedules,
        'working_days': working_days,
    }
    return render(request, 'schedule.html', context)


def create_working_day(request):
    if request.method == 'POST':
        form = WorkingDaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workingdays_list')
    else:
        form = WorkingDaysForm()
    return render(request, 'create_working_day.html', {'form': form})


def home_view(request):
    return render(request, 'base.html')


def calendar_view(request):
    return render(request, 'calendar.html')


@csrf_exempt
def api_events(request):
    if request.method == 'GET':
        # Obtenha os parâmetros 'start' e 'end' da query string
        start = request.GET.get('date_start')
        end = request.GET.get('date_finish')

        # Valide se os valores foram passados
        if not start or not end:
            return JsonResponse({'error': 'Os parâmetros "start" e "end" são obrigatórios.'}, status=400)

        # Ajuste os valores para conter apenas a data no formato 'YYYY-MM-DD'
        start_date = start.split('T')[0]
        end_date = end.split('T')[0]

        # Filtrar eventos dentro do intervalo fornecido
        events = WorkingDays.objects.filter(
            date_start__gte=start_date, date_finish__lte=end_date)
        events_list = [
            {
                'id': event.id,
                'title': event.observation,
                'start': event.date_start.isoformat(),
                'end': event.date_finish.isoformat(),
                'technic': event.technic_id,
                'customer': event.customer_id,
                'servic': event.servic_id,
                'color': '#007bff',
            }
            for event in events
        ]
        return JsonResponse(events_list, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        event = WorkingDays.objects.create(
            observation=data['title'],
            date_start=data['date_start'],
            date_finish=data['date_finish'],
            technic_id=data['technician'],
            customer_id=data['customer'],
            servic_id=data['service']
        )
        return JsonResponse({'id': event.id}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        event = WorkingDays.objects.get(id=data['id'])
        event.date_start = data['date_start']
        event.date_finish = data['date_finish']
        event.save()
        return JsonResponse({'success': True}, status=200)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        event = WorkingDays.objects.get(id=data['id'])
        event.delete()
        return JsonResponse({'success': True}, status=200)
