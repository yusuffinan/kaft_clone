from django.contrib import admin
from django.urls import include, path
from kaft_clone import settings
from page.views import index
from django.conf.urls.static import static
from cart.views import shopping_cart_item_add, view_shopping_cart,remove_from_cart,add_back_to_cart

urlpatterns = [
    path('<int:cart_item_id>/', shopping_cart_item_add, name='shopping_cart_item_add'),
    path('view_shopping_cart/', view_shopping_cart, name='view_shopping_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('add_back_to_cart/<int:item_id>/', add_back_to_cart, name='add_back_to_cart'),
]

