from django.contrib import admin
from .models import Comment
from shop.models import Product

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'comment', 'product', 'createdAt')
	list_filter = ('createdAt',)
	search_fields = ('author', 'comment')