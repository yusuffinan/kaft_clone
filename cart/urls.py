from django.contrib import admin
from django.urls import include, path
from kaft_clone import settings
from page.views import index
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<int:cart_item_id>/', views.shopping_cart_item_add, name='shopping_cart_item_add'),
    path('view_shopping_cart/', views.view_shopping_cart, name='view_shopping_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_back_to_cart/<int:item_id>/', views.add_back_to_cart, name='add_back_to_cart'),
    path('clear/', views.clear_shopping_cart, name='clear_shopping_cart'),

]

