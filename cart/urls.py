from . import views
from django.urls.conf import path
# from categories.models import Categories

urlpatterns = [
    path('', views.cart, name="carts"),
    path('add_cart/<int:product_id>/', views.add_cart, name="add_cart"),
    # path('<slug:categories_slug>/', views.store, name="product_by_categories"),
    
    # path('<slug:categories_slug>/<slug:product_slug>/',
    #      views.product_detail,
    #      name="product_detail"),
]
