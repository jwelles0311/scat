from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms

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
    template_name = 'clientes_create.html'
    form_class = forms.ClientesFrom
    success_url = reverse_lazy('clientes_list')


class ClientesDetailView(DetailView):
    model = models.Companies
    template_name = 'clientes_detail.html'


class ClientesUpdateView(UpdateView):
    model = models.Companies
    template_name = 'clientes_update.html'
    form_class = forms.ClientesFrom
    success_url = reverse_lazy('clientes_list')


class ClientesDeleteView(DeleteView):
    model = models.Companies
    template_name = 'clientes_delete.html'
    success_url = reverse_lazy('clientes_list')
