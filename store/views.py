from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
# from django.urls import Exception
from store.models import Products
from categories.models import Categories

# Create your views here.

    # function for store page
def store(request, categories_slug=None):
    category1 = None
    product = None

    if (categories_slug != None):
        category1 = get_object_or_404(Categories, slug=categories_slug)
        product = Products.objects.filter(categories=category1, available=True)
        product_count = product.count()
    else:
        product = Products.objects.all().filter(available=True)
        product_count = product.count()
    param = {
        'products': product,
        'count': product_count,
    }
    return render(request, 'store.html', param)



# def store1(request, products_slug=None):
#     product_to_add = None
#     product = None

#     if (products_slug != None):
#         product_to_add = get_object_or_404(Products, slug=products_slug)
#         product = Products.objects.filter(product_name=product_to_add, available=True)
#         product_count = product.count()
#     else:
#         product = Products.objects.all().filter(available=True)
#         product_count = product.count()
#     param = {
#         'products': product,
#         'count': product_count,
#     }
#     return render(request, 'product_home.html', param)



    # function for single product page 
def product_detail(request, categories_slug, product_slug):
    try:
        single_product = Products.objects.get(categories__slug=categories_slug,
                                          slug=product_slug)
        print("hello")
    except Exception as exceptions:
        raise exceptions

    param1 = {"single_product": single_product}
    return render(request, 'product.html', param1)


# def store(request):
#     return render(request,'store.html')


def search(request):
    if 'keyword' in request.GET:
        keyword=request.GET["keyword"]
        # prod=Products.objects.filter(description__icontains=keyword)
        prod=Products.objects.filter(product_name__icontains=keyword)
        count=prod.count()
    param={
        'products':prod,
        'count':count
    }
    return render(request, 'store.html', param)
        
        