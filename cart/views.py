from django.shortcuts import render, redirect
from .models import ShopingCart, ShopingCartItem
# Create your views here.

def shopping_cart_item_add(request,cart_item_id):
    if request.user.is_authenticated:
        user = request.user
        shopping_cart = ShopingCart.objects.filter(user = user, status="waiting")
        if shopping_cart.count() > 0:
            shopping_cart = shopping_cart.last()
        else:
            shopping_cart = ShopingCart.objects.create(user=user)
        shopping_cart.session_key = request.session.session_key
        item = ShopingCartItem.objects.get(pk=cart_item_id)
        shopping_cart.items.add(item)
        shopping_cart.total_price_update()
        shopping_cart.save()
    return redirect("/")

def view_shopping_cart(request):
    if request.user.is_authenticated:
        user = request.user
        shopping_cart = ShopingCart.objects.filter(user=user, status="waiting").last()
        if shopping_cart:
            return render(request, 'view_shopping_cart.html', {'shopping_cart': shopping_cart})
    return render(request, 'view_shopping_cart.html') 

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        item = ShopingCartItem.objects.get(pk=item_id)
        print(f"Removing item: {item}")
        if not item.is_deleted:
            item.is_deleted = True
            item.save()
            print(f"Item {item} is_deleted: {item.is_deleted}")
            
            shopping_cart_instance = item.shopingcart_set.first()
            if shopping_cart_instance is not None:
                shopping_cart_instance.total_price_update()
                print(f"Total price updated: {shopping_cart_instance.total_price}")
    
    return redirect('view_shopping_cart')

def add_back_to_cart(request, item_id):
    if request.method == 'POST':
        item = ShopingCartItem.objects.get(pk=item_id)
        if item.is_deleted:
            item.is_deleted = False
            item.save()

            shopping_cart_instance = item.shopingcart_set.first()
            if shopping_cart_instance is not None:
                shopping_cart_instance.total_price_update()

    return redirect('view_shopping_cart')
