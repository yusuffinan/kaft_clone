from django.urls import path
from page.views import carousel_list, carousel_create, carousel_update

urlpatterns = [
path("carousel_create",carousel_create, name="carousel_create"),
path("carousel_list",carousel_list, name="carousel_list")
    
]

