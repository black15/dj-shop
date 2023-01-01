from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ('email', 'first_name', 'last_name' ,'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Info', {'fields': ('first_name', 'last_name', 'phone', 'birthday')}),
        ('Picture', {'fields': ('picture',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2', 'is_staff', 'is_active', 'picture')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Account, CustomUserAdmin)