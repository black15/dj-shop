from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, View

from django.urls import reverse

from .models import Account
from .forms import RegistrationForm, LoginForm

class LoginView(View):

	template_name 	= 'account/login.html'
	form_class 		= LoginForm

	def get(self, request):
		form = self.form_class()
		message = ''
		return render(request, self.template_name, context={'form': form, 'message': message})

	def post(self, request, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password'],
			)
			if user is not None:
				login(request, user)
				return redirect('shop:all_products')
			message = 'Login failed!'
			return render(request, self.template_name, context={'form': form, 'message': message})

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

class ProfileView(LoginRequiredMixin, UpdateView):
	login_url = '/user/login/'
	model = Account
	fields = ['first_name', 'last_name', 'phone', 'birthday', 'picture']
	template_name = "account/profile.html"
	
	def get_success_url(self):
		return reverse('account:profile', kwargs={'pk': self.request.user.id})
		
	def dispatch(self, request, *args, **kwargs):
		if request.user.id == int(self.kwargs.get('pk')):
			return super().dispatch(request, *args, **kwargs)
		return redirect('shop:all_products')