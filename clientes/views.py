from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class ClientesListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Companies
    template_name = 'clientes_list.html'
    context_object_name = 'clientes'
    paginate_by = 5
    permission_required = 'clientes.view_companies'

    def get_queryset(self):
        queryset = super().get_queryset()
        corporate_reason = self.request.GET.get('corporate_reason')

        if corporate_reason:
            queryset = queryset.filter(
                corporate_reason__contains=corporate_reason)
        return queryset


class ClientesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Companies
    template_name = 'clientes_create.html'
    form_class = forms.ClientesFrom
    success_url = reverse_lazy('clientes_list')
    permission_required = 'clientes.add_companies'


class ClientesDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Companies
    template_name = 'clientes_detail.html'
    permission_required = 'clientes.view_companies'


class ClientesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Companies
    template_name = 'clientes_update.html'
    form_class = forms.ClientesFrom
    success_url = reverse_lazy('clientes_list')
    permission_required = 'clientes.change_companies'


class ClientesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Companies
    template_name = 'clientes_delete.html'
    success_url = reverse_lazy('clientes_list')
    permission_required = 'clientes.delete_companies'
