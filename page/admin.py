from django.contrib import admin
from .models import Page
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("pk","title", "status",)
    prepopulated_fields = {"slug": ("title",),}