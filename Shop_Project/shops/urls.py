from django.contrib import admin
from django.urls import path

from .views import registerShop, home, searchShops, ShopListCreateView


urlpatterns = [
    path('register/',registerShop, name='register_shop'),
    path('search/', searchShops, name='searchShops'),
    path('api/shops/', ShopListCreateView.as_view(), name='api_shops'),
    path("",home, name="homePage"),
]
