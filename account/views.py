from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from account.models import Account
from django.shortcuts import redirect, render
from .form import RegistrationForm
# Create your views here.


def dashboard(request):
    return render(request, 'account/dashboard.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        flag = True
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            username = email.split('@')[0]

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
                user = Account.objects.create_user(first_name=first_name, last_name=last_name,
                                                   email=email, username=username)
                user.phone_no = phone_no
                user.set_password('password')
                user.save()
            # user.phone_no = phone_no
            # user.save()
            # print(request.POST.get("email"))
            # form.save()

            # user activation
            # current_site=get_current_site(request)
            # mail_subject='Please activate your account'
            # message=render_to_string
            # messages.success(request, )
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

        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        print(request)
        user = authenticate(request, Username=email, password=password)
        print(user)
        print("ssssssssssssss")

        if user is not None:
            login(request, user)
            print("aaaaaaaaaa")
            return redirect('home')

        else:
            str = "Invaild LOgIN Credentials"
            param = {
                "error": str,
            }
            print("jjjjjjjjjjjjjj")
            return redirect('login_account')

    return render(request, 'account/login.html')


def logout(request):
    return render(request, 'home.html')
