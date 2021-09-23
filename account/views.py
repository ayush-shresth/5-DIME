
from account.models import Account, MyAccountManager
from django.shortcuts import render
from .form import RegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            password = form.cleaned_data['password']

            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                               email=email, username=username, password=password,)
            user.phone_no = phone_no
            user.save()
    else:
        form = RegistrationForm()
        param = {
            'form': form,
        }
    return render(request, 'account/register.html', param)


def login(request):
    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'account/register.html')
