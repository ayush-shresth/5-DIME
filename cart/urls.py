from . import views
from django.urls.conf import path
# from categories.models import Categories

urlpatterns = [
    path('', views.cart, name="carts"),
    path('add_cart/<int:product_id>/', views.add_cart, name="add_cart"),
    path('decrement_item/<int:product_id>/', views.decrement_item, name="decrement_item"),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name="remove_cart_item"),
    # path('<slug:categories_slug>/', views.store, name="product_by_categories"),
    
    # path('<slug:categories_slug>/<slug:product_slug>/',
    #      views.product_detail,
    #      name="product_detail"),
]
