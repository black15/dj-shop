from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from .models import Account

# Admin panel user creation & modification forms
class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ('email',)
class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = Account
		fields = ('email',)

# Register new user form
class RegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'text-gray-700 w-80 md:w-96 rounded'}))

	class Meta:
		model = Account
		fields = ("first_name", "last_name", "email", "phone", "password")
		widgets = {
            'first_name': forms.TextInput(attrs={'class': 'text-gray-700 w-80 md:w-96 rounded'}),
            'last_name': forms.TextInput(attrs={'class': 'text-gray-700 w-80 md:w-96 rounded'}),
            'email': forms.EmailInput(attrs={'class': 'text-gray-700 w-80 md:w-96 rounded'}),
            'phone': forms.TextInput(attrs={'class': 'text-gray-700 w-80 md:w-96 rounded'}),
        }
	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'first_name', 'last_name', 'phone', 'birthday', 'picture', 'is_staff', 'is_superuser')

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'phone', 'birthday', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]