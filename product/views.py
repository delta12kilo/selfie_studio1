from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products, Contact
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from cart.cart import Cart
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.


#home
def Home(request):
  

    return render(request, "product/home.html")

#product view main page
def product(request):
    cat = request.GET.get('DATA')
    if cat:
        product = Products.objects.filter(cat=cat)
    else:
        product = Products.objects.all()

    return render(request, "product/products.html", {'product': product} )

   
@login_required(login_url='login')
def contact_us(request):

    if request.method == "POST":

        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    messages.success(request, 'Your qury sent  successfully!')
    return render(request, "contact.html")


#checkout (payment ) page 
@login_required(login_url='login')
def checkout(request):
    return render(request, "checkout.html")

#search page
def search(request):
    search = request.GET.get('search')
    if search:
        search_res = Products.objects.filter(name__contains=search)
    else:
        search_res = Products.objects.filter(cat__contains=search)

    return render(request, "search.html", {'search_res': search_res})

#view detail page 
def show_product(request, id):
    pro = Products.objects.all()
    product = Products.objects.get(id=id)

    return render(request, "product/showproduct.html", {"product": product,  'pro': pro})


@login_required
def cart_add(request, id):
    
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("product")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    
    return render(request, 'cart/cart_detail.html')


