from django.db import models
from django.urls import reverse

# Create your models here.

class Categories(models.Model):
    categories_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    categories_desc = models.TextField(max_length=300, blank=True)
    categories_img = models.ImageField(upload_to ='photos/categories', blank=True)
    created_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='Categories'
        verbose_name_plural='Categories'
    
    def get_url(self):
        return(reverse('product_by_categories', args=[self.slug] ))
    

    def __str__(self):
        return self.categories_name
