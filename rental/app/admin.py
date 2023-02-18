from django.contrib import admin

from .models import Product,ProdBookingDetails
# Register your models here.


admin.site.register(Product)
admin.site.register(ProdBookingDetails)