"""greatkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from store import views as v
from store import urls
from cart import urls

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/',include('store.urls')),
    path('cart/',include('cart.urls')),
    path('<slug:categories_slug>/', v.store, name="product_by_categories"),#####
    # path('<slug:products_slug>/', v.store1, name="products_by_product"),
    #  path('<slug:categories_slug>/<slug:store_slug>/',
    #      views.h,
    #      name="product_detail"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
