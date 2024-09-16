
# orders/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'orders/user_orders.html', {'orders': orders})