from django.db import models
from shop.models import Product
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):

	product 		= models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, related_name="comments")
	author 		= models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
	comment 		= models.TextField(_("Comment"))
	# rating 		= models.IntegerField(_("Rating"), default=0)
	createdAt 	= models.DateTimeField("Created At", auto_now_add=True)

	class Meta:
		ordering = ['createdAt']
		verbose_name = _("Comment")
		verbose_name_plural = _("Comments")

	def __str__(self):
		return f"Comment by {self.author} on {self.product}"
