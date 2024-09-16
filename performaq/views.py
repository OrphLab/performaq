from django.shortcuts import render
from django.http import HttpResponse
from product.models import Tag, Product
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def index(request):
    tags = Tag.objects.all()[:11]
    product = Product.objects.all()
    return render(request, 'performaq/index.html', {'tags':tags,'product':product})



