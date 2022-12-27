from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', products_list, name='all_products'),
    path('<slug:category_slug>/', products_list, name="products_by_category"),
    path('product/<int:id>/<slug:slug>', product_details, name="product_by_id")
]
