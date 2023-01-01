from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

class AccountManager(BaseUserManager):
	"""
		Custom user model manager where email is the unique identifiers
		for authentication instead of usernames.
	"""
	def create_user(self, email, first_name, last_name, phone, password, **extra_fields):
		"""
        Create and save a User with the given email and password.
		"""
		if not email:
			raise ValueError('Email is required')
		if not first_name:
			raise ValueError('First name is required')
		if not last_name:
			raise ValueError('Last name is required')
		if not phone:
			raise ValueError('Phone number is required')
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		email = self.normalize_email(email)
		user 	= self.model(
			email=email, 
			first_name=first_name, 
			last_name=last_name, 
			phone=phone, 
			**extra_fields
		)
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self, email, password, **extra_fields):
		"""
        Create and save a SuperUser with the given email and password.
		"""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
	email 		= models.EmailField('Email', max_length=254, unique=True)
	first_name 	= models.CharField(max_length=50, blank=False, null=False)
	last_name 	= models.CharField(max_length=50, blank=False, null=False)
	phone			= models.CharField("Phone Number", max_length=16)
	picture 		= models.ImageField("User picture", upload_to='uploads/accounts/images/%Y/%m/%d', null=True)
	birthday 	= models.DateField(blank=True, null=True)
	is_staff 	= models.BooleanField("Staff", 	default=False)
	is_active 	= models.BooleanField("Active", 	default=False)
	date_joined = models.DateField(auto_now_add=True)

	USERNAME_FIELD 	= 'email'
	REQUIRED_FIELDS 	= ['first_name', 'last_name', 'phone']

	objects 	= AccountManager()

	def __str__(self):
		 return self.email
	def get_full_name(self):
		return f'{first_name} {last_name}'