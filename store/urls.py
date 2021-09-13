from . import views
from django.urls.conf import path
from categories.models import Categories

urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:categories_slug>/', views.store, name="product_by_categories"),
    
    path('<slug:categories_slug>/<slug:product_slug>/',
         views.product_detail,
         name="product_detail"),
]
