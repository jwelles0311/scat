

from django.urls import path
from .views import calendar_view, WorkingDaysCalendarView
from . import views

urlpatterns = [
    path('list/', views.workingdays_list, name='workingdays_list'),
    path('create/', views.create_working_day, name='create_working_day'),
    path('update/<int:pk>/', views.update_working_day, name='update_working_day'),
    path('delete/<int:pk>/', views.delete_working_day, name='delete_working_day'),
    path('calendar/', calendar_view, name='calendar'),
    path('api/calendar/', WorkingDaysCalendarView.as_view(), name='calendar-api'),
]
