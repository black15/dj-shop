from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductImages
from cart.forms import CartAddProductForm

def products_list(request, category_slug=None):
   context     = {} 
   category    = None
   categories  = Category.objects.all()
   products    = Product.available_only.all()
   if category_slug:
      category = get_object_or_404(Category, slug=category_slug)
      products = Product.available_only.filter(category=category)

   context['category']   = category
   context['categories'] = categories
   context['products']   = products

   return render(request, 'shop/product/list.html', context)

def product_details(request, id, slug):
   context = {}
   categories  = Category.objects.all()
   product = get_object_or_404(Product, id=id, slug=slug, available=True)
   
   add_to_cart = CartAddProductForm()
   
   context['product'] = product
   context['categories'] = categories
   context['add_product_to_cart'] = add_to_cart
   context['product_images'] = ProductImages.objects.filter(product=product)
   
   return render(request, 'shop/product/details.html', context)