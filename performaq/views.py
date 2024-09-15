from django.shortcuts import render
from django.http import HttpResponse
from product.models import Tag, Product

# Create your views here.

def index(request):
    tags = Tag.objects.all()[:11]
    product = Product.objects.all()
    return render(request, 'performaq/index.html', {'tags':tags,'product':product})
