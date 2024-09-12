from django.shortcuts import render
from django.http import HttpResponse
from product.models import Tag

# Create your views here.

def index(request):
    #tags = Tag.objects.all()
    tags = Tag.objects.all()[:11]
    return render(request, 'performaq/index.html', {'tags':tags})
