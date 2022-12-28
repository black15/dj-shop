from django.contrib import admin
from .models import Category, Product, ProductImages

class PostImageAdmin(admin.StackedInline):
    model = ProductImages

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name', 'slug']
   prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display   = ['name', 'slug', 'price', 'available', 'createdAt', 'updatedAt']
   list_filter    = ['available', 'createdAt', 'updatedAt']
   list_editable  = ['price', 'available']
   list_display_links = ('name',)
   prepopulated_fields  = {'slug': ('name',)}
   inlines = [PostImageAdmin]