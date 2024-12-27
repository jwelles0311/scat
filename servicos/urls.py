from django.urls import path
from . import views

urlpatterns = [
    path('servicos/list/', views.ServicosListView.as_view(), name='servicos_list'),
    path('servicos/create/', views.ServicosCreateView.as_view(),
         name='servicos_create'),
    path('servicos/<int:pk>/detail/',
         views.ServicosDetailView.as_view(), name='servicos_detail'),
    path('servicos/<int:pk>/update/',
         views.ServicosUpdateView.as_view(), name='servicos_update'),
    path('servicos/<int:pk>/delete/',
         views.ServicosDeleteView.as_view(), name='servicos_delete'),
]
