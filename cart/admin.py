from django.contrib import admin
from .models import ShopingCart, ShopingCartItem


admin.site.register(ShopingCart)
admin.site.register(ShopingCartItem)

# # Register your models here.
# @admin.register(ShopingCart)
# class ShoppingCartAdmin(admin.ModelAdmin):
#     list_display = ("product", "price",)
    
# @admin.register(ShopingCartItem)
# class ShoppingItemAdmin(admin.ModelAdmin):
#     list_display = ("status",)