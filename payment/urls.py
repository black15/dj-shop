from django.urls import path
from .views import *

app_name = 'payment'

urlpatterns = [
    path('process/', payment_process, name='process'),
    path('config/', stripe_config, name='stripe_config'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('done/', payment_done, name='done'),
    path('cancelled/', payment_cancelled, name='cancelled'),
]
