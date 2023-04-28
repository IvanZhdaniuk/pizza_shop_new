
from django.contrib import admin
from django.urls import path
from pizzashop_app import views

urlpatterns = [

    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('index/<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),

]
