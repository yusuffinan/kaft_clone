from django.contrib import admin
from .models import Product, Category
# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("pk","title", "slug","status","uploated_at",)
    list_filter = ("status",)
    list_editable = ("title", "status",)
    prepopulated_fields = {"slug": ("title",),}

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("pk","title", "slug","price", "stock", "status","uploated_at",)
    list_filter = ("status",)
    list_editable = ("title", "status",)
    prepopulated_fields = {"slug": ("title",),}