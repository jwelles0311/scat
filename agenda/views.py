from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import WorkingDaysForm, WorkingDaysDayForm
from .models import WorkingDays

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.db.models import Q, Count
from clientes.models import Companies
from tecnicos.models import Technicians

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WorkingDaysSerializer


# Create (já fornecido antes)


@login_required(login_url='/login/')
def create_working_day(request):
    if request.method == 'POST':
        form = WorkingDaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workingdays_list')
    else:
        form = WorkingDaysForm()

    return render(request, 'create_working_day.html', {'form': form})


# Read (Listar todos os agendamentos)

@login_required(login_url='/login/')
def workingdays_list(request):
    technicians = Technicians.objects.all()
    customers = Companies.objects.all()

    # Filtros
    technician_id = request.GET.get('technician')
    customer_id = request.GET.get('customer')
    date_start = request.GET.get('date_start')
    date_finish = request.GET.get('date_finish')
    status = request.GET.get('status')

    workingdays = WorkingDays.objects.all()

    if technician_id:
        workingdays = workingdays.filter(technician_id=technician_id)
    if customer_id:
        workingdays = workingdays.filter(customer_id=customer_id)
    if date_start:
        workingdays = workingdays.filter(date_start__gte=date_start)
    if date_finish:
        workingdays = workingdays.filter(date_finish__lte=date_finish)
    if status:
        workingdays = workingdays.filter(status=status)

    return render(request, 'workingdays_list.html', {
        'workingdays': workingdays,
        'technicians': technicians,
        'customers': customers,
    })


# Update (Atualizar um agendamento)

@login_required(login_url='/login/')
def update_working_day(request, pk):
    working_day = get_object_or_404(WorkingDays, pk=pk)

    if request.method == 'POST':
        form = WorkingDaysDayForm(request.POST, instance=working_day)
        if form.is_valid():
            form.save()
            return redirect('workingdays_list')
    else:
        form = WorkingDaysDayForm(instance=working_day)
        print(f"Editing: date_start={working_day.date_start}, date_finish={
              working_day.date_finish}")

    return render(request, 'update_working_day.html', {
        'form': form,
        'working_day': working_day,
    })

# Delete (Excluir um agendamento)


@login_required(login_url='/login/')
def delete_working_day(request, pk):
    working_day = get_object_or_404(WorkingDays, pk=pk)
    if request.method == 'POST':
        working_day.delete()
        return redirect('workingdays_list')

    return render(request, 'delete_working_day.html', {'working_day': working_day})


@login_required(login_url='/login/')
def home_view(request):
    return render(request, 'base.html')


def calendar_view(request):
    return render(request, 'calendar.html')


# views.py


class WorkingDaysCalendarView(LoginRequiredMixin, APIView):
    def get(self, request, *args, **kwargs):
        events = WorkingDays.objects.all()
        serializer = WorkingDaysSerializer(events, many=True)

        # Formatar os dados para o FullCalendar
        formatted_events = [
            {
                "id": event['id'],
                "title": f"{event['technician_name']}",  # Nome do técnico
                "start": event['date_start'],

                # Adicionando a descrição do serviço
                "description": event['service_service'],
                "cliente": event['customer_corporate_reason'],
            }
            for event in serializer.data
        ]
        return Response(formatted_events)


def technician_report(request):
    technicians = Technicians.objects.all()  # Carregar todos os técnicos

    technician_id = request.GET.get('technician')
    date_start = request.GET.get('date_start')
    date_finish = request.GET.get('date_finish')

    report = None
    if technician_id and date_start and date_finish:
        report = WorkingDays.objects.filter(
            technician_id=technician_id,
            date_start__gte=date_start,
            date_finish__lte=date_finish,
            status="CONCLUIDO"
        ).annotate(total_services=Count('service'))

    return render(request, 'reports/technician_report.html', {
        'technicians': technicians,
        'report': report
    })
