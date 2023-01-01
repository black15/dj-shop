from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import Account
from .forms import RegistrationForm

class LoginAccountView(LoginView):
	template_name = 'account/login.html'

class RegisterAccountView(CreateView):
	template_name 	= 'account/register.html'
	form_class 		= RegistrationForm

	def get_context_data(self, **kwargs):
		 context = super(RegisterAccountView, self).get_context_data(**kwargs)
		 context["next"] = self.request.GET.get('next')
		 return context
	def get_success_url(self):
		next_url 	= self.request.POST.get('next')
		success_url = reverse('account:login')
		if next_url:
			success_url += f'?next={next_url}'
		return success_url

class ProfileView(CreateView):
	model = Account
	fields = ('first_name', 'last_name', 'phone', 'birthday', 'picture')
	template_name = "account/profile.html"

	def get_success_url(self):
		return reverse('index')
	def get_object(self):
		return self.request.user
