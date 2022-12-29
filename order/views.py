from datetime import datetime

from django.urls import reverse
from django.shortcuts import render, redirect

from .models import OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from order.tasks import order_created

def order_create(request):
   cart = Cart(request)
   if request.method == 'POST':
      form = CreateOrderForm(request.POST)
      if form.is_valid():
         order = form.save()
         for item in cart:
            OrderItem.objects.create(
               order=order,
               product=item['product'],
               price=item['price'],
               quantity=item['quantity'])
         cart.clear()
         order_created.delay(order.id)
         
         # Async task
         request.session['order_id'] = order.id

         return redirect(reverse('payment:process'))
   else:
      form = CreateOrderForm()
      return render(request, 'order/create.html', {'cart':cart, 'form': form})
      
   