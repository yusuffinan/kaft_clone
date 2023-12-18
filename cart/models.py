from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

STATUS=[
    ('buyed','Alindi'),
    ('deleted','Silindi'),
    ('waiting','Bekleniyor'),

]

class ShopingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.product.title } price: { self.product.price }tl"
    
  
    
class ShopingCart(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    items= models.ManyToManyField(ShopingCartItem, blank=True)
    total_price = models.FloatField(default=0)
    status = models.CharField(default="waiting", choices=STATUS, max_length=10,)
    created_at = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f" pk: { self.pk } - total: { self.total_price } - status: { self.status }"
    
    def total_price_update(self):
         if self.status == "waiting":
            total_price=0
            for item in self.items.all():
                if item.is_deleted == False:
                    total_price += item.price
            self.total_price = total_price
            self.save() 

@receiver(post_save, sender=ShopingCartItem)
def shopping_cart_receiver(sender, instance, created, *args, **kwargs):
        if created:
             instance.price = instance.product.price
             instance.save()
        shopping_cart_instance = instance.shopingcart_set.first()
        if shopping_cart_instance is not None:
            shopping_cart_instance.total_price_update()
        print(sender)
        print(kwargs)

@receiver(m2m_changed, sender=ShopingCart.items.through)
def shopping_cart(sender, instance, *args, **kwargs):
     instance.total_price_update()
     print(args)
     print(kwargs)