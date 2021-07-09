from django.contrib import admin
from django.urls import path
from django_practice_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home, name="index"),
    path('home/', views.home, name="index"),
    path('', views.home, name="index"),
]
