from categories.models import Categories
from store.models import Products
from django.shortcuts import render


def home(request):

    product = Products.objects.all().filter(available=True)
    param={'products':product}
    return render(request, 'home.html', param)