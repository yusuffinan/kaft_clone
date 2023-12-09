from django.shortcuts import render,redirect
from .models import Carousel
from django.contrib import messages
from .forms import CarouselModelFrom
def index(request):
    context = dict()
    context['images'] = Carousel.objects.all()
    return render(request, 'home/index.html', context)

def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all()
    return render (request, "manage/carousel_list.html", context)

def carousel_update(request,pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['form'] = CarouselModelFrom(instance=item)
    if request.method == "POST":
        form = CarouselModelFrom(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("carousel_list")
    return render (request, "manage/carousel_update.html", context)

def carousel_create(request):
    context = dict()
    context["form"]= CarouselModelFrom()
    if request.method == "POST":
        form = CarouselModelFrom(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        messages.success(request, "Ne eklendiği bilinmiyor")
        return redirect("carousel_list")

    return render(request, "manage/carousel_create.html", context)
