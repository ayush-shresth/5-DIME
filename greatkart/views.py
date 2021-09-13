from categories.models import Categories
from store.models import Products
from django.shortcuts import render
from store.views import product_detail



def home(request):
    product = Products.objects.all().filter(available=True)
    param={'products':product}
    return render(request, 'home.html', param)

def h(request, c, s):
     product_detail(request, categories_slug = c, store_slug = s)