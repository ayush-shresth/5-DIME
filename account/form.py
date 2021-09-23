from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your First Name',
        'class': 'form-control',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Last Name',
        'class': 'form-control',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Your Email',
        'class': 'form-control',
    }))

    phone_no = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter Your Contact No.',
        'class': 'form-control',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'password', ]
