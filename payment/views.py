import stripe
import environ

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from order.models import Order, OrderItem

env = environ.Env()
environ.Env.read_env()


def payment_process(request):
	try:
		if request.session['order_id']:			
			return render(request, 'payment/paypage.html')
	except KeyError:
		return redirect('shop:all_products')

def payment_done(request):
	try:
		if request.session['order_id']:
			del request.session['order_id']
			return render(request, 'payment/done.html')
	except KeyError:
		return redirect('shop:all_products')

def payment_cancelled(request):
	try:
		if request.session['order_id']:
			del request.session['order_id']
			return render(request, 'payment/cancelled.html')
	except KeyError:
		return redirect('shop:all_products')

@csrf_exempt
def stripe_config(request):
	if request.method == 'GET':
		stripe_conf = {'stripe_pk': settings.STRIPE_PUBLISHABLE_KEY}
		return JsonResponse(stripe_conf, safe=False)

@csrf_exempt
def create_checkout_session(request):
	order = get_object_or_404(Order, id=request.session['order_id'])
	order.paid = True
	order.save()
	total_order_cost = order.get_total_cost()
	item  = get_object_or_404(OrderItem, order=order.id)
	if request.method == 'GET':
		domain_url = env('BASE_URL')
		stripe.api_key = settings.STRIPE_SECRET_KEY
		try:
			checkout_session = stripe.checkout.Session.create(
				success_url=domain_url + 'payment/done?session_id={CHECKOUT_SESSION_ID}',
				cancel_url=domain_url + 'payment/cancelled/',
				payment_method_types=['card'],
				mode='payment',
				line_items=[{
					'price_data': {
						'currency': 'usd',
						'unit_amount': int(total_order_cost),
						'product_data': {
							'name': item.product,
						},
					},
					'quantity': 1,
				}]
			)
			return JsonResponse({'sessionId': checkout_session['id']})
		except Exception as e:
			return JsonResponse({'error': str(e)})
