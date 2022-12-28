from django import forms
from .models import Order, OrderItem

class CreateOrderForm(forms.ModelForm):
   class Meta:
      model    = Order
      fields   = ['first_name', 'last_name', 'email', 'adress', 'city', 'postal_code',]
      
   def __init__(self, *args, **kwargs):
      className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      emailClass="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      super().__init__(*args, **kwargs)
      self.fields['first_name'].widget.attrs.update({'class': className, 'placeholder': 'Oussama'})
      self.fields['last_name'].widget.attrs.update({'class': className, 'placeholder': 'Dev'})
      self.fields['email'].widget.attrs.update({'class': emailClass, 'placeholder': 'web@dev123.com'})
      self.fields['adress'].widget.attrs.update({'class': className, 'placeholder': 'whatever'})
      self.fields['city'].widget.attrs.update({'class': className, 'placeholder': 'Algiers'})
      self.fields['postal_code'].widget.attrs.update({'class': className, 'placeholder': '000000'})