from datetime import datetime

from django.urls import reverse
from django.shortcuts import render, redirect

from .models import OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from order.tasks import order_created

def order_create(request):
   cart = Cart(request)
   if cart.get_total_quantities() > 0:
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
            # Async task
            order_created.delay(order.id)

            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
      else:
         form = CreateOrderForm()
         return render(request, 'order/create.html', {'cart':cart, 'form': form})
   else:
      return(redirect('shop:all_products'))
   