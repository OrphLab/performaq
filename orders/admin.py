from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    
    list_display=('user', 'product')  
    
    search_fields=('user__username',)
admin.site.register(Order, OrderAdmin)