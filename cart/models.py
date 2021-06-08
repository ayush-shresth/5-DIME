from django.db import models
from django.db.models.fields import BooleanField
from store.models import Products

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=200, blank=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id


class CartItems(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name='CartItems'
        verbose_name_plural='Cart Items'

    def __str__(self) -> str:
        return self.product
