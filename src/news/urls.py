from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name="scraper"),
    path('task-status/', views.task_status, name='task_status'),
    path('task-view/', views.task_view, name='task_view'),
]
