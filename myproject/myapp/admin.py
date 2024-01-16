from django.contrib import admin
from .models import category,customer,product,order 

class ProductAdmin(admin.ModelAdmin): # new
    readonly_fields = ['img_preview']   
# Register your models here.
admin.site.register(category)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)