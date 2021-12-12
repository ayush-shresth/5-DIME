from django.urls import reverse
from categories.models import Categories
from django.db import models

# Create your models here.


class Products(models.Model):

    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=3000, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="photos/product")
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"

    def get_url(self):
        return reverse("product_detail", args=[self.categories.slug, self.slug, ])

    def __str__(self):
        return self.product_name
