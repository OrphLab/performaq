# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.user_orders, name='user_orders'),
]