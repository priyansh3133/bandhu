"""genesisportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .views import signup,signup_success_admin,activate,login_user,signup_success,activated,not_activated,signup_failure,change_password

urlpatterns = [
    path('activated/', activated,name="activatedpage"),
    path('signup_success_admin/', signup_success_admin,name="adminsuccesspage"),
    path('activationerror/', not_activated,name="not_activatedpage"),
    path('signup/success/', signup_success,name="signup_success_page"),
    path('signup/failure/', signup_failure,name="signup_failure_page"),
    path('signup/', signup,name="signuppage"),
    path('activate/<uidb64>[0-9A-Za-z_\-]/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/', activate, name='activate'),
    path('login/', login_user, name="loginpage"),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html/'),name='logoutpage', kwargs={'next_page':'homepage'}),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/reset_password.html'),name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(template_name='registration/passwordresetdone.html'),name='password_reset_done'),
    path('reset/<uidb64>[0-9A-Za-z_\-]/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/', PasswordResetConfirmView.as_view(template_name='registration/passwordresetconfirm.html'),name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/passwordresetcomplete.html'), name="password_reset_complete"),
    path('change_password/', change_password, name='change_password'),
]
