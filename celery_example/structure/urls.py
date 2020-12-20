from django.urls import path
from celery_example.structure import views


urlpatterns = [
    path('', views.msg, name='message')
]
