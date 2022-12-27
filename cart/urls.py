from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_details, name="cart_content"),
    path("add/<int:product_id>", add_to_cart, name="add_cart_item"),
    path("remove/<int:product_id>", remove_from_cart, name="remove_cart_item")
]
