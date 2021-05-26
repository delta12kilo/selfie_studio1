from django.contrib import admin
from product.models import Products,Category,Cart,Purchase,Contact
admin.site.site_header = "Seflie studio "


class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','quantity','discount','cat']










# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Contact)
admin.site.register(Purchase)
