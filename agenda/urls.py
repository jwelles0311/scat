# urls.py
"""from django.urls import path
from . import views


urlpatterns = [
    path('schedule/', views.technician_schedule_view, name='technician_schedule'),
    path('create_working_day/', views.create_working_day,
         name='create_working_day'),
]
"""
from django.urls import path
from . import views
from .views import WorkingDaysListView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('agendamentos/', WorkingDaysListView.as_view(), name='workingdays_list'),
    #   path('schedule/', views.technician_schedule_view, name='technician_schedule'),
    path('create-working-day/', views.create_working_day,
         name='create_working_day'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('api/events/', views.api_events, name='api_events'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
