from django.views.generic import ListView
from . import models

# Create your views here.

class ClientesListView(ListView):
    model = models.Companies
    template_name = 'clientes_list.html'
    context_object_name = 'clientes'


