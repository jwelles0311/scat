from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView
from . import models

# Create your views here.


class ClientesListView(ListView):
    model = models.Companies
    template_name = 'clientes_list.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        queryset = super().get_queryset()
        corporate_reason = self.request.GET.get('corporate_reason')

        if corporate_reason:
            queryset = queryset.filter(
                corporate_reason__contains=corporate_reason)
        return queryset


class ClientesCreateView(CreateView):
    model = models.Companies
    template_name = 'clientes_list.html'
    context_object_name = 'clientes'
