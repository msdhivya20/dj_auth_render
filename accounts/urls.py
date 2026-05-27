from django.urls import path
from django.contrib.auth import views

from .views import *

urlpatterns=[

path(
'',
home,
name='home'
),

path(
'signup/',
signup,
name='signup'
),

path(
'login/',
login_view,
name='login'
),

path(
'dashboard/',
dashboard,
name='dashboard'
),

path(
'logout/',
logout_view,
name='logout'
),

path(
'password-reset/',
views.PasswordResetView.as_view(
template_name=
'password_reset.html'
),
name='password_reset'
),

path(
'password-reset-done/',
views.PasswordResetDoneView.as_view(
template_name=
'password_reset_done.html'
),
name='password_reset_done'
),

path(
'reset/<uidb64>/<token>/',
views.PasswordResetConfirmView.as_view(
template_name=
'password_reset_confirm.html',

success_url=
'/reset-complete/'
),
name='password_reset_confirm'
),

path(
'reset-complete/',
views.PasswordResetCompleteView.as_view(
template_name=
'password_reset_complete.html'
),
name='password_reset_complete'
),

path(
'forgot-username/',
forgot_username,
name='forgot_username'
),

path(
'profile/',
upload_profile,
name='profile'
),

]