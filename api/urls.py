from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('task-list/', views.task_list, name='task-list'),
    path('task-detail/<str:pk>/', views.task_detail, name='task-detail'),
    path('task-create/', views.task_create, name='task-create'),
    path('task-update/<str:pk>/', views.task_update, name='task-update'),
    path('task-delete/<str:pk>/', views.task_delete, name='task-delete')
]


urlpatterns = format_suffix_patterns(urlpatterns)
