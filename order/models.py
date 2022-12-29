from django.db import models
from shop.models import Product

class Order(models.Model):
   first_name     = models.CharField(max_length=50) 
   last_name      = models.CharField(max_length=50)
   email          = models.EmailField(max_length=254)
   adress         = models.CharField(max_length=50)
   postal_code    = models.CharField(max_length=50)
   city           = models.CharField(max_length=50)
   createdAt      = models.DateTimeField(auto_now_add=True)
   updatedAt      = models.DateTimeField(auto_now=True)
   paid           = models.BooleanField(default=False)
   braintree_id   = models.CharField(max_length=150, blank=True)
   
   class Meta:
      ordering = ('-createdAt',)
   
   def __str__(self):
       return f'Order {self.id}'
   def get_total_cost(self):
      return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
   order    = models.ForeignKey("Order", verbose_name="Order", on_delete=models.CASCADE, related_name='items')
   product  = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, related_name='order_items')
   price    = models.DecimalField(max_digits=10, decimal_places=2)
   quantity = models.PositiveIntegerField(default=1)

   def __str__(self):
       return str(self.id)
   def get_cost(self):
      return self.price * self.quantity
   
   