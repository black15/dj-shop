from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import *

@require_POST # Accept only post request
def add_to_cart(request, product_id):
   cart     = Cart(request)
   product  = get_object_or_404(Product, id=product_id)
   form     = CartAddProductForm(request.POST)
   if form.is_valid():
      cleaned_data = form.cleaned_data
      cart.add(
         product=product, 
         quantity=cleaned_data['quantity'], 
         override_quantity=cleaned_data['override']
         )
   return redirect('cart:cart_content')

@require_POST
def remove_from_cart(request, product_id):
   cart     = Cart(request)
   product  = get_object_or_404(Product, id=product_id)
   cart.remove(product)
   return redirect('cart:cart_content')

def cart_details(request):
   cart     = Cart(request)
   for item in cart:
      item['update_quantity_form'] = CartAddProductForm(initial={
         'quantity': item['quantity'],
         'override': True,
      })
   return render(request, 'cart/details.html', {'cart': cart})