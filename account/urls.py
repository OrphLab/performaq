from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="accountindex"),
    path("buy/<int:product_id>/", views.buy_product, name="buy_product"),
]