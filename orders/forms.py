from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        """Meta definition for Orderform."""
        model = Order
        fields = ["first_name", "last_name", "phone_number", "email", "address_line_1","address_line_2", "city", "state", "pin_code", "order_note"]
