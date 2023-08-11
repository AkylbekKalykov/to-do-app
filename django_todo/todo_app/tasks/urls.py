from django.urls import path
from .import views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_tasks, name='add_task'),
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name='mark_as_done')
]