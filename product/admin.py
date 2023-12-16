from django.contrib import admin
from .models import Product, Category
# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("pk","title", "slug","gender","status","uploated_at",)
    list_filter = ("status","gender",)
    list_editable = ("title", "status",)
    prepopulated_fields = {"slug": ("title",),}

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("pk","title","category", "slug", 
                    "cover_image", "is_home","price", "stock", "status","uploated_at",)
    list_filter = ("status",)
    list_editable = ("title", "status","is_home",)
    prepopulated_fields = {"slug": ("title",),}