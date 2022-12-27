from django.db import models
from django.urls import reverse

# Model Class
class Category(models.Model):
   name     = models.CharField(max_length=50, blank=False, unique=True, db_index=True)
   slug     = models.SlugField(max_length=200, unique=True)
   fawesome = models.CharField(max_length=50, blank=True)

   class Meta:
      ordering = ('name',)
      verbose_name = 'Category'
      verbose_name_plural = 'Categories'

   def get_absolute_url(self):
       return reverse("shop:products_by_category", args=[self.slug])
   
   def __str__(self):
       return self.name

# Model Class
class AvailableProducts(models.Manager):
   def get_queryset(self):
        return super().get_queryset().filter(available=True)

# Model Class
class Product(models.Model):
   category    = models.ForeignKey("Category", related_name='products', on_delete=models.CASCADE)
   name        = models.CharField(max_length=50, db_index=True) 
   slug        = models.SlugField(max_length=200, db_index=True, unique=True)
   image       = models.ImageField(upload_to='products/%Y/%m/%d')
   description = models.TextField(blank=True)
   price       = models.DecimalField(max_digits=10, decimal_places=2)
   available   = models.BooleanField(default=True)
   createdAt   = models.DateTimeField(auto_now_add=True)
   updatedAt   = models.DateTimeField(auto_now=True)
   
   objects        = models.Manager() 
   available_only = AvailableProducts()
   

   class Meta:
      ordering = ('name',)
      index_together = (('id', 'slug'),)

   def get_absolute_url(self):
       return reverse("shop:product_by_id", args=[self.id, self.slug])
   
   def __str__(self):
       return self.name
   