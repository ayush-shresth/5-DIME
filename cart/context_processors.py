from .models import Cart, CartItem
from .views import _cart_id

# def _cart_id(request):
#     cart_data = request.session.session_key
#     if not cart_data:
#         cart_data = request.session.create()

#     # print(cart_data)
#     return cart_data
def counter(request):
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart_count=0
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cartItem in cart_items:
                cart_count += cartItem.quantity
        except Cart.DoesNotExist:
            cart_count=0
    return {"cart_count":cart_count}

