from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms

# Create your views here.


class TecnicosListView(ListView):
    model = models.Technicians
    template_name = 'tecnicos_list.html'
    context_object_name = 'tecnicos'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(
                corporate_reason__contains=name)
        return queryset


class TecnicosCreateView(CreateView):
    model = models.Technicians
    template_name = 'tecnicos_create.html'
    form_class = forms.TecnicosForm
    success_url = reverse_lazy('tecnicos_list')


class TecnicosDetailView(DetailView):
    model = models.Technicians
    template_name = 'tecnicos_detail.html'


class TecnicosUpdateView(UpdateView):
    model = models.Technicians
    template_name = 'tecnicos_update.html'
    form_class = forms.TecnicosForm
    success_url = reverse_lazy('tecnicos_list')


class TecnicosDeleteView(DeleteView):
    model = models.Technicians
    template_name = 'tecnicos_delete.html'
    success_url = reverse_lazy('tecnicos_list')
