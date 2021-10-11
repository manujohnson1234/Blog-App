from django.urls import path

from .views import UserRegisterView, UserEditProfile, PasswordsChangeView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register-page/', UserRegisterView.as_view(), name='register-page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/', UserEditProfile.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), {'post_change_Redirect': 'edit_profile'}, name='change_password'),
]