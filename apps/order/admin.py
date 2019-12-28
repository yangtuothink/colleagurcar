from django.contrib import admin

# Register your models here.
from order.models import Order, DriverSquare, CustomerSquare

admin.site.register(Order)
admin.site.register(DriverSquare)
admin.site.register(CustomerSquare)
