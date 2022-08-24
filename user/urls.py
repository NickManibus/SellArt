from django.urls import path, include
from user.views import RegisterView, log_out, LogLoginView, ChangePasswordView, PostCreateView, Profile
from django.shortcuts import redirect
from django.urls import reverse
from user.forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("login/", LogLoginView.as_view(redirect_authenticated_user=True, authentication_form=LoginForm),
         name="login_page"),
    path('signin/', RegisterView.as_view(), name='signin_page'),
    path('logout/', log_out, name='logout_page'),
    path('profile/<slug:slug>/', Profile.as_view(), name='users_profile'),
    path('profile/create_post', PostCreateView.as_view(), name='create_post'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('', lambda request: redirect(reverse('login_page'))),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

]
