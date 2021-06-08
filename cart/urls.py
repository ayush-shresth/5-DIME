from django import urls
from django.urls.conf import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
]
