from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart',  {})
    if not cart:
        messages.error(request, "Nothing in your cart for now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IHVefBxhZFkfOwatK6EEB4HaMHfEn8vnPqFmXlzvZhVP5TrxTG1ON3Pm48A8fiXvVRBIkaS7bNTtHwf2Kxyeanq000s7Fr71Q',
        'client_secret': 'test client_secret,'
    }

    return render(request, template, context)
