from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products, Contact, Cart
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


def count_cart_items(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
        print(count)
        return count
    else:
        return 0


def Home(request):
    #products= Products.objects.all()

    return render(request, "product/home.html")


def product(request):
    cat = request.GET.get('DATA')
    if cat:
        product = Products.objects.filter(cat=cat)
    else:
        product = Products.objects.all()

    return render(request, "product/products.html", {'product': product, 'cart_count': count_cart_items(request)})


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


@login_required(login_url='login')
def checkout(request):
    return render(request, "checkout.html")


def search(request):
    search = request.GET.get('search')
    print(search)
    search_res = Products.objects.filter(name__contains=search)

    return render(request, "search.html", {'search_res': search_res})


def show_product(request, id):
    pro = Products.objects.all()
    product = Products.objects.get(id=id)

    return render(request, "product/showproduct.html", {"product": product, 'cart_count': count_cart_items(request), 'pro': pro})


@login_required(login_url='login')
def add_to_cart(request):
    pid = request.GET.get('pid')
    product = Products.objects.get(pk=pid)
    cart = Cart(user=request.user, product=product)
    cart.save()
    return redirect('product')


def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.price)
                amount += tempamount
                totalamount = amount+shipping_amount

            return render(request, "product/addtocart.html", {'cart': cart, "totalamount": totalamount, 'amount': amount})

        else:
            return render(request, "product/emptycart.html")


def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.price)
            amount += tempamount
            totalamount = amount+shipping_amount

        data = {
                    'quantity': c.quantity,
                    'amount': amount,
                    'totalamount': totalamount
                }
        return JsonResponse(data)
