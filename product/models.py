from django.db import models
from page.models import STATUS_DEFAULT, STATUS
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", db_index=True, blank=True, unique=True, null= False, max_length=200)
    status = models.CharField(default=STATUS_DEFAULT, choices=STATUS, max_length=10)
    created_att = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", db_index=True, blank=True, unique=True, null= False, max_length=200)
    status = models.CharField(default=STATUS_DEFAULT, choices=STATUS, max_length=10)
    content = models.TextField()
    created_att = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveSmallIntegerField(default=0)
    price = models.FloatField()
    def __str__(self):
        return f"{self.title}"