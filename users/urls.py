from django.contrib import admin
from django.urls import path
from .views import register, new, user_status
from . import views

urlpatterns = [
      path('users/', views.register, name='users-register'),
      path('users/', views.new, name='users-new'),
      path('users/', views.user_status, name='users-user_status'),
      #path('users/', views.new, name='users-new'),

     ]

