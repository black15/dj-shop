from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
   def __init__(self, request):
      # Initialize the cart session
      self.session = request.session
      cart = self.session.get(settings.CART_SESSION_ID)
      if not cart:
         cart = self.session[settings.CART_SESSION_ID] = {}
      self.cart = cart

   def __iter__(self):
      # Iterate over the items in the cart and get the products from the database.
      product_ids = self.cart.keys()
      products    = Product.available_only.filter(id__in=product_ids)
      # Copy the current cart.
      cart        = self.cart.copy()
      # add the Product instances to the copied
      for product in products:
         cart[str(product.id)]['product'] = product
      for item in cart.values():
         item['price'] = Decimal(item['price'])
         item['total_price'] = item['price'] * item['quantity']
         yield item

   # def __len__(self):
   #    # Count all items in the cart
   #    return sum(item['quantity'] for item in self.cart.values())

   def add(self, product, quantity=1, override_quantity=False):
      # Add a product to the card or update it's quantity
      product_id = str(product.id)
      if product_id not in self.cart:
         self.cart[product_id] = {
            'quantity': 0,
            'price'   : str(product.price), 
         }
      if override_quantity:
         self.cart[product_id]['quantity']  = quantity
      else:
         self.cart[product_id]['quantity'] += quantity
      self.save()

   def save(self):
      self.session.modified = True # This tells Django that the session has changed and needs to be saved

   def remove(self, product):
      # Remove product from the cart
      product_id = str(product.id)
      if product_id in self.cart:
         del self.cart[product_id]
         self.save()

   def clear(self):
      # Remove the cart from session
      del self.session[settings.CART_SESSION_ID]
      self.save()

   def get_total_price(self):
      return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

   def get_total_quantities(self):
      return sum(item['quantity'] for item in self.cart.values())