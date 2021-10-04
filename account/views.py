from django.contrib import messages
from django.contrib.auth.models import User, auth

from account.models import Account
from django.shortcuts import redirect, render
from .form import RegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        flag = True
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # phone_no = form.cleaned_data['phone_no']
            # password = form.cleaned_data['password']
            # print(form.email)
            username = request.POST.get("email").split('@')[0]
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone_no = request.POST.get("phone_no")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            # user = Account( username=username,)
            print(len(password))
            

            if len(phone_no) < 10:
                flag = False
                form.add_error('phone_no',
                               'Phone Number should be of 10 digits!!!')

            flag_pass = True
            if len(password) < 6:
                flag = False
                flag_pass = False
                form.add_error('password',
                               'Password should be of 6 digits!!!')

            if (confirm_password != password) and flag_pass:
                flag = False
                form.add_error('confirm_password',
                               'Password does not matched!!!')

            if flag:
                #    flag_success_msg = True
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                               email=email, username=username, password=password, phone_no=phone_no)
                # form.add_error(
                #     'first_name', 'Registration is successfull!!!  LogIn to Continue')
                # print(form.errors)

                # def my_view(request):
                #     if form.is_valid():
                #         messages.success(request, 'Form submission successful')

                user.save()
            # user.phone_no = phone_no
            # user.save()
            # print(request.POST.get("email"))
            # form.save()

        param = {
            'form': form,
            'flag': flag,
        }
    else:
        form = RegistrationForm()
        param = {
            'form': form,
            'flag': False,
        }

    return render(request, 'account/register.html', param)


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login_account')

    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'account/register.html')
