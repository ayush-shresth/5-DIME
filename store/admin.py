from django.contrib import admin
from .models import Products


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'price',
        'stock',
        'categories',
        'created_date',
        'available',
    )

    list_editable = ('available', 'stock', 'price',)

    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Products, ProductAdmin)
