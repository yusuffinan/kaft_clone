from django.db import models
from product.models import Product
from django.contrib.auth.models import User

STATUS=[
    ('buyed','Alindi'),
    ('deleted','Silindi'),
    ('waiting','Bekleniyor'),

]

class ShopingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)

class ShopingCart(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    items= models.ManyToManyField(ShopingCartItem, blank=True)
    total_price = models.FloatField()
    status = models.CharField(default="waiting", choices=STATUS, max_length=10,)
    created_at = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)