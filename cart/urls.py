from django.contrib import admin
from django.urls import include, path
from kaft_clone import settings
from page.views import index
from django.conf.urls.static import static
from cart.views import shopping_cart_item_add

urlpatterns = [
    path('<int:cart_item_id>/', shopping_cart_item_add, name='shopping_cart_item_add'),
]

