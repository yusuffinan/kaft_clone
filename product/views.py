from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from page.views import STATUS
# Create your views here.

def category_show(request, category_slug):
    context = dict()
    context['category']= get_object_or_404(Category, slug=category_slug)
    # context['categories'] = Category.objects.filter(status=STATUS)

    context['items'] = Product.objects.filter(
        category=context['category'],
        status = "published",
        stock__gte=1,
    )
    return render(request, "product/category_show.html", context)