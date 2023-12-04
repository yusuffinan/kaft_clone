from django.contrib import admin
from .models import Page, Carousel
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("pk","title", "status",)
    list_filter = ("status",)
    list_editable = ("title", "status",)
    prepopulated_fields = {"slug": ("title",),}

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ("title",)