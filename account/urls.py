from django.urls.conf import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register_account"),
    path('login/', views.login, name="login_account"),
    path('logout/', views.logout, name="logout_account"),
]
