from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class ServicosListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Services
    template_name = 'servicos_list.html'
    context_object_name = 'servicos'
    permission_required = 'servicos.view_services'

    def get_queryset(self):
        queryset = super().get_queryset()
        service = self.request.GET.get('service')

        if service:
            queryset = queryset.filter(
                corporate_reason__contains=service)
        return queryset


class ServicosCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Services
    template_name = 'servicos_create.html'
    form_class = forms.ServicosForm
    success_url = reverse_lazy('servicos_list')
    permission_required = 'servicos.add_services'


class ServicosDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Services
    template_name = 'servicos_detail.html'
    permission_required = 'servicos.view_services'


class ServicosUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Services
    template_name = 'servicos_update.html'
    form_class = forms.ServicosForm
    success_url = reverse_lazy('servicos_list')
    permission_required = 'servicos.change_services'


class ServicosDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Services
    template_name = 'servicos_delete.html'
    success_url = reverse_lazy('servicos_list')
    permission_required = 'servicos.delete_services'
