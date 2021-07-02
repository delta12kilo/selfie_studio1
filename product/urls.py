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
   path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
   path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
   path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
   path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
   path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
   path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
