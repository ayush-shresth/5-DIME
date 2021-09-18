from django.db import models
from store.models import Products
# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=300, blank=True)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=100)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.product_name
    
    def total_cost(self):
        return self.quantity * self.product_name.price

    