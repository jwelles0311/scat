from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms

# Create your views here.


class ServicosListView(ListView):
    model = models.Services
    template_name = 'servicos_list.html'
    context_object_name = 'servicos'

    def get_queryset(self):
        queryset = super().get_queryset()
        service = self.request.GET.get('service')

        if service:
            queryset = queryset.filter(
                corporate_reason__contains=service)
        return queryset


class ServicosCreateView(CreateView):
    model = models.Services
    template_name = 'servicos_create.html'
    form_class = forms.ServicosForm
    success_url = reverse_lazy('servicos_list')


class ServicosDetailView(DetailView):
    model = models.Services
    template_name = 'servicos_detail.html'


class ServicosUpdateView(UpdateView):
    model = models.Services
    template_name = 'servicos_update.html'
    form_class = forms.ServicosForm
    success_url = reverse_lazy('servicos_list')


class ServicosDeleteView(DeleteView):
    model = models.Services
    template_name = 'servicos_delete.html'
    success_url = reverse_lazy('servicos_list')
