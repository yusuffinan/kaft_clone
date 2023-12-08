from django.shortcuts import render
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
    context['carousel'] = Carousel.objects.all()
    context['item'] = Carousel.objects.get(pk=pk)
    return render (request, "manage/carousel_update.html", context)

def carousel_create(request):
    context = dict()
    context["form"]= CarouselModelFrom()
    if request.method == "POST":
        print (request.POST)
        print(request.FILES.get('cover_image'))
        messages.success(request, "Ne eklendiği bilinmiyor")
    return render(request, "manage/carousel_create.html", context)
