from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('create/', order_create, name='create'),
]
