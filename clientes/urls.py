from django.urls import path
from . import views

urlpatterns = [
    path('clientes/list', views.ClientesListView.as_view(), name='clientes_list'),
]