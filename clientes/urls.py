from django.urls import path
from . import views

urlpatterns = [
    path('clientes/list/', views.ClientesListView.as_view(), name='clientes_list'),
    path('clientes/create/', views.ClientesCreateView.as_view(),
         name='clientes_create'),
    path('clientes/<int:pk>/detail/',
         views.ClientesDetailView.as_view(), name='clientes_detail'),
    path('clientes/<int:pk>/update/',
         views.ClientesUpdateView.as_view(), name='clientes_update'),

    path('clientes/<int:pk>/delete/',
         views.ClientesDeleteView.as_view(), name='clientes_delete'),

]
