from django.shortcuts import render, HttpResponse, redirect
from .forms import OrderForm
from cart.views import _cart_id
import datetime
from .models import Order, Payment
from cart.models import CartItem, Cart
# Create your views here.



def place_order(request):
    # cart_items=CartItem.objects.filter()
    cart_data = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.filter(cart=cart_data, is_available=True)
    cart_count = cart_item.count()

    if cart_count <= 0:
        return redirect('store')

    total = 0
    quantity = 0
    for item in cart_item:
        total += (item.product_name.price * item.quantity)
        quantity += item.quantity

    tax = (total*8)/100
    grand_total = tax+total

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()

            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.phone_number = form.cleaned_data['phone_number']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.pin_code = form.cleaned_data['pin_code']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # generate order no.
            current_date_time = datetime.datetime.now()
            unique_no = str(current_date_time.year) + str(current_date_time.month)+str(current_date_time.day)+str(
                current_date_time.hour)+str(current_date_time.minute)+str(current_date_time.second)+str(current_date_time.microsecond)

            data.order_number = unique_no+str(data.id)
            data.save()

            param={
                "first_name":data.first_name,
                "last_name":data.last_name,
                "email":data.email,
                "phone_number":data.phone_number,
                "address_line_1":data.address_line_1,
                "address_line_2":data.address_line_2,
                "city":data.city,
                "state":data.state,
                "pin_code":data.pin_code,
                "order_note":data.order_note,
                "grand_total":grand_total,
                "tax":tax,
                "total":total,
                "order_number":data.order_number,
                "cart_items":cart_item,
            }
            return render(request, "order_placed.html", param)
    else:
        return redirect('checkout')

def payments(request):
    # body=json.loads(request.body)
    # ordert=Order.objects.get(order_number=body['orderId'])
    # payment=Payment(
    #     user=request.user,
    #     payment_id=body['transId'],
    #     payment_method=body['payment_method'],
    #     amount_paid=order.order_total,
    #     status=body['status'],
    # )
    # payment.save()
    # order.payment=payment
    # order.is_order=True
    # order.save()

    
    return render(request, 'checkout.html')
