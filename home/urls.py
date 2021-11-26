from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Api Url
    path('', views.student_api, name='student-api'),
    path('student-list/', views.student_list, name='student-list'),
    path('student-create/', views.student_create, name='student-create'),

]
