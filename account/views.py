from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import Product
from orders.models import Order
# Create your views here.

def index(request):
    return HttpResponse("Account index here")
    

@login_required
def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Add the product to the user's bought_products
    if request.user not in product.buyers.all():
        product.buyers.add(request.user)
        product.save()
        # Create an order record
        Order.objects.create(user=request.user, product=product, quantity=1, status='Completed')
        messages.success(request, 'Product successfully added to your account and order placed!')
    else:
        messages.warning(request, 'You already own this product.')

    return redirect('user_orders')

