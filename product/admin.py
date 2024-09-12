from django.contrib import admin
from .models import Product, ProductFile, Tag

class ProductAdmin(admin.ModelAdmin):
    list_display = ('creator', 'name', 'price') 
    search_fields = ('name',)  
admin.site.register(Product, ProductAdmin)

class ProductFileAdmin(admin.ModelAdmin):
    list_display = ('product', 'file') 
admin.site.register(ProductFile, ProductFileAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  
admin.site.register(Tag, TagAdmin)
