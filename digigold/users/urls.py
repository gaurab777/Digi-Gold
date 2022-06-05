from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',
		auth_views.LoginView.as_view(template_name='users/login.html'),
		name='users_login'),
	
    path('logout/',
		auth_views.LogoutView.as_view(template_name='users/logout.html'),
		name='users_logout'),

    path('register/',
		views.userRegister,
		name='users_register'),

    path('profile/',
		views.userProfile, 
		name='users_profile'),

    path('aboutus/',
		views.aboutUs, 
		name='about_us'),

    path('contactus/',
		views.contactUs, 
		name='contact_us'),

    path('password-reset/',
		auth_views.PasswordResetView.as_view(template_name='users/pass_reset.html'),
		name='password_reset'),

    path('password-reset/confirm/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(template_name='users/pass_reset_confirm.html'),
		name='password_reset_confirm'),

    path('password-reset/complete/',
		auth_views.PasswordResetDoneView.as_view(template_name='users/pass_reset_comp.html'),
		name='password_reset_complete'),

    path('password-reset/done/',
		auth_views.PasswordResetDoneView.as_view(template_name='users/pass_reset_done.html'),
		name='password_reset_done'),
]
