from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import RegisterAccountView, ProfileView, LoginView

app_name = "account"

urlpatterns = [
	path('register/', RegisterAccountView.as_view(), name='register'),
	path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]