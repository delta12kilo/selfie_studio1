from django.contrib import admin
from django.urls import path,include
from .views import create_checkout_session,purchase_item
from payments import views
from os import name
urlpatterns = [
    path('purchase/',purchase_item,name="purchase"),
    path("config/",views.stripe_config, name='config'),
    path('create-checkout-session/',views.create_checkout_session,name='create_checkout_session'),
    path('success/',views.notify_success,name='success'),
    path('cancelled/',views.notify_cancelled,name='cancelled'),
]