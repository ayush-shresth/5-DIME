from django.core.exceptions import ObjectDoesNotExist
from store.models import Products
from django.shortcuts import redirect, render
from .models import Cart, CartItem


def _cart_id(request):
    cart_data = request.session.session_key
    if not cart_data:
        cart_data = request.session.create()

    # print(cart_data)
    return cart_data


def add_cart(request, product_id):
    # print(product_id)

    product_to_add = Products.objects.get(id=product_id)
    # print(product_to_add)

    try:
        cart_products = Cart.objects.get(cart_id=_cart_id(request))

    except Cart.DoesNotExist:
        cart_products = Cart.objects.create(
            cart_id=_cart_id(request)
        )

    cart_products.save()

    try:
        cart_item_product = CartItem.objects.get(
            product_name=product_to_add,
            cart=cart_products
        )

        cart_item_product.quantity += 1
        # print(cart_item_product.quantity)

        cart_item_product.save()

    except CartItem.DoesNotExist:
        cart_item_product = CartItem.objects.create(
            product_name=product_to_add,
            cart=cart_products,
            quantity=1,
        )
        cart_item_product.save()

    return redirect(cart)


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart_data = Cart.objects.get(cart_id =_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart_data, is_available=True)
        # pro=Products.objects.filter(product_name=cart_items)
        # for i in pro:
        #     total+=i.price** item.quantity
        for item in cart_items:
            total += (item.product_name.price * item.quantity)
            quantity += item.quantity

    except ObjectDoesNotExist:
        pass
    tax=(total*8)/100
    grand_total=tax+total
    param = {"total": total,
             "quantity": quantity,
             "cart_items": cart_items,
             "tax":tax,
             "grand_total":grand_total,
             }
    return render(request, 'cart.html', param)
