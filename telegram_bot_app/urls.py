
from django.contrib import admin
from django.urls import path
from telegram_bot_app import views

urlpatterns = [

    path('', views.form_page, name='form-page'),


]
