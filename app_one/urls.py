from django.contrib.auth import views as auth_views
from django.urls import path
from app_one.views import *

app_name = "app_one"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("currency/", view_currency, name="currency"),
    path("get-currency/", get_currency, name="get_currency"),

    path('login/', auth_views.LoginView.as_view(template_name='app_one/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("register/", RegisterView.as_view(), name="register"),
]

htmx_urlpatters = [
    path("check-username/", check_username, name='check-username'),
]

urlpatterns += htmx_urlpatters
