from django.urls import path
from . import views

urlpatterns = [
    path('tecnicos/list/', views.TecnicosListView.as_view(), name='tecnicos_list'),
    path('tecnicos/create/', views.TecnicosCreateView.as_view(),
         name='tecnicos_create'),
    path('tecnicos/<int:pk>/detail/',
         views.TecnicosDetailView.as_view(), name='tecnicos_detail'),
    path('tecnicos/<int:pk>/update/',
         views.TecnicosUpdateView.as_view(), name='tecnicos_update'),
    path('tecnicos/<int:pk>/delete/',
         views.TecnicosDeleteView.as_view(), name='tecnicos_delete'),
]
