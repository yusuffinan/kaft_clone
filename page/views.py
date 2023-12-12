from django.shortcuts import render,redirect
from .models import Carousel, Page
from django.contrib import messages
from .forms import CarouselModelForm, PageModelForm
from django.utils.text import slugify
def index(request):
    context = dict()
    context['images'] = Carousel.objects.all()
    return render(request, 'home/index.html', context)

def manage_list(request):
    context = dict()
    return render(request, "manage/manage.html", context)


def page_create(request):
    context = dict()
    context["title"] = "Page Create"
    context["form"]= PageModelForm()
    if request.method == "POST":
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
           item = form.save(commit=False)
           item.slug = slugify(item.title.replace('ı', 'i'))
           item.save()
        return redirect("page_list")

    return render(request, "manage/form.html", context)

def page_update(request,pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    context['form'] = PageModelForm(instance=item)
    if request.method == "POST":
        form = PageModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item= form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace("ı", "i"))
            item.save()
            return redirect("page_list")
    return render (request, "manage/form.html", context)

def page_delete(request, pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    form = PageModelForm(request.POST, request.FILES, instance=item)
    if request.method == "POST":
        form.delete()
    return redirect("page_list")

def page_list(request):
    context = dict()
    context['items'] = Page.objects.all()
    return render (request, "manage/page_list.html", context)

def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all()
    return render (request, "manage/carousel_list.html", context)

def carousel_update(request,pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['form'] = CarouselModelForm(instance=item)
    if request.method == "POST":
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("carousel_list")
    return render (request, "manage/form.html", context)

def carousel_create(request):
    context = dict()
    context["form"]= CarouselModelForm()
    if request.method == "POST":
        form = CarouselModelForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        messages.success(request, "Ne eklendiği bilinmiyor")
        return redirect("carousel_list")

    return render(request, "manage/form.html", context)
