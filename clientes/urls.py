from django.urls import path
from . import views

urlpatterns = [
    path('clientes/list', views.ClientesListView.as_view(), name='clientes_list'),
    path('clientes/create', views.ClientesCreateView.as_view(),
         name='clientes_create'),
]
