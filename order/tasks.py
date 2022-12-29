from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
	"""Sends an email when the feedback form has been submitted."""

	order = Order.objects.get(id=order_id)
	subject = f'DjShop Order nr. {order.id}'
	message = f'Dear {order.first_name},\n\nYou have successfully placed an order. \nYour order ID is {order.id}.'
	mail_sent = send_mail(subject, message, 'admin@djshop.com', [order.email])

	return mail_sent