from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path("", views.Home, name="home"),
   path("product", views.product, name="product"),
   path("show_product/<int:id>",views.show_product,name="show_product"),
   path("contact_us",views.contact_us,name="contact_us"),
   path("search",views.search,name="search"),
   path("checkout",views.checkout,name="checkout"),
   path("addcart",views.add_to_cart,name="add_to_cart"),
   path("showcart",views.showcart,name="showcart"),
   path('pluscart',views.plus_cart,name="plus_cart"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
