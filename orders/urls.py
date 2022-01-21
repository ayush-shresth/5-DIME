from . import views
from django.urls.conf import path


urlpatterns = [
    path('place_order/', views.place_order, name="place_order"),
    path('payments/', views.payments, name="payments"),
    
]
