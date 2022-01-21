from django.contrib import admin
from .models import Payment,OrderProduct,Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=['order_number','first_name','email','phone_number']
    list_per_page=20


admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)