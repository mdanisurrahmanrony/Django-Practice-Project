from django.conf.urls import url
from django.urls import path
from django_practice_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),  
]
