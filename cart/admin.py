from django.contrib import admin
from django.contrib.admin import sites
from .models import Cart, CartItem
# Register your models here
admin.site.register(Cart)
admin.site.register(CartItem)