from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductImages
from cart.forms import CartAddProductForm
from comment.models import Comment
from comment.forms import CommentForm

def products_list(request, category_slug=None):
   context     = {} 
   category    = None
   categories  = Category.objects.all()
   products    = Product.available_only.all()
   recent      = Product.available_only.all().order_by('-updatedAt')[:5]
   if category_slug:
      category = get_object_or_404(Category, slug=category_slug)
      products = Product.available_only.filter(category=category)
      recent   = Product.available_only.filter(category=category).order_by('-updatedAt')[:5]

   context['category']   = category
   context['categories'] = categories
   context['products']   = products
   context['recent']     = recent

   return render(request, 'shop/product/list.html', context)

def product_details(request, id, slug):
   context = {}
   categories  = Category.objects.all()
   product = get_object_or_404(Product, id=id, slug=slug, available=True)
   comments = Comment.objects.filter(product=product)
   
   add_to_cart = CartAddProductForm()
   
   if request.method == "POST":
      form = CommentForm(data=request.POST)
      if form.is_valid():
         new_comment = form.save(commit=False)
         new_comment.product = product
         new_comment.author = request.user
         new_comment.save()
   else:
      form = CommentForm()

   context['form'] = form

   context['product'] = product
   context['comments'] = comments
   context['categories'] = categories
   context['add_product_to_cart'] = add_to_cart
   context['product_images'] = ProductImages.objects.filter(product=product)
   
   return render(request, 'shop/product/details.html', context)