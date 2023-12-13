from django.urls import path
# from page.views import carousel_list, carousel_create, carousel_update,manage_list, page_list
from . import views

urlpatterns = [
path("", views.manage_list, name="manage_list"),
path("carousel_create", views.carousel_create, name="carousel_create"),
path("carousel_list", views.carousel_list, name="carousel_list"),
path("page_list", views.page_list, name="page_list"),
path("page_create", views.page_create, name="page_create"),

path("carousel_update/<int:pk>", views.carousel_update, name="carousel_update"),
path("page_update/<int:pk>", views.page_update, name="page_update"),
path("page_delete/<int:pk>", views.page_delete, name="page_delete")



    
]

