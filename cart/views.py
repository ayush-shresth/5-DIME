from store.models import Products
from .models import Cart, CartItems
from django.http.response import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product1 = Products.objects.get(id=product_id)
    try:
        cart1 = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart1 = Cart.objects.create(
            cart_id1=cart_id(request)
        )
    cart1.save()

    try:
        cart_item = CartItems.objects.get(product=product1, cart=cart1)
        cart_item.quantity += 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart1 = CartItems.objects.create(
            product=product1,
            quantity=1,
            cart=cart1,)
        cart_item.save()
    # return HttpResponse(cart_item.quantity)
    # exit()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_item=None):
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItems.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            quantity += cart_item.quantity
        total = (cart_item.product.price * cart_item.quantity)
    except Exception:
        pass
    context = {'total': total, 'item': cart_items, 'quant': quantity}
    # return HttpResponse(quantity)
    return render(request, 'cart.html', context)
