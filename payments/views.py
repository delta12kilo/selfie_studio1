from django.shortcuts import render
from django.http.response import JsonResponse
from payments.forms import PurchaseForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from cart.cart import Cart
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from user.models import Adderss
from .models import PurchaseModel
import stripe
# Create your views here.


def purchase_item(request):
    add = Adderss.objects.filter(user=request.user)
    return render(request, "payment.html", {'add': add})


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = "http://127.0.0.1:8000/"
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # product data
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url +
                'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url+'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    'name': 'ABCD',
                    'quantity': 5,
                    'currency': 'inr',
                    'amount': 200020,  # Rs  2000 and 20 paise
                }]
            )
            cart = Cart(request)
            cart.clear()
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def notify_success(request):
    messages.success(request, f"Your payment is complete.")
    return redirect('home')


def notify_cancelled(request):
    messages.error(request, f"Your payment is cancelled.")
    return redirect('cart_detail')
