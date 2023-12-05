from django import forms
from .models import Carousel

class CarouselModelFrom(forms.ModelForm):
    class Meta:
        model = Carousel
        fields=["title", "cover_image", "status"]