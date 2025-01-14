from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class TecnicosListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Technicians
    template_name = 'tecnicos_list.html'
    context_object_name = 'tecnicos'
    permission_required = 'tecnicos.view_technicians'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(
                corporate_reason__contains=name)
        return queryset


class TecnicosCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Technicians
    template_name = 'tecnicos_create.html'
    form_class = forms.TecnicosForm
    success_url = reverse_lazy('tecnicos_list')
    permission_required = 'tecnicos.add_technicians'


class TecnicosDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Technicians
    template_name = 'tecnicos_detail.html'
    permission_required = 'tecnicos.view_technicians'


class TecnicosUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Technicians
    template_name = 'tecnicos_update.html'
    form_class = forms.TecnicosForm
    success_url = reverse_lazy('tecnicos_list')
    permission_required = 'tecnicos.change_technicians'


class TecnicosDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Technicians
    template_name = 'tecnicos_delete.html'
    success_url = reverse_lazy('tecnicos_list')
    permission_required = 'tecnicos.delete_technicians'
