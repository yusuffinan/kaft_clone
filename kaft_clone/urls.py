from django.contrib import admin
from django.urls import include, path
from kaft_clone import settings
from page.views import index
from django.conf.urls.static import static
from product.views import category_show

urlpatterns = [
    path("", index, name="index"),
    path("<slug:category_slug>", category_show, name="category_show" ),
    path('admin/', admin.site.urls),
    path('manage/', include('page.urls'),),
    path('cart/', include('cart.urls')),  # cart/1/ gibi URL'leri ele alaca

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

