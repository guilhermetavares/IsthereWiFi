# -*- coding: utf-8 -*-
from .views import GoogleLoginView, LoginView, RegistrationView, FacebookLoginView
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='accounts_login'),
    url(r'^cadastre-se/$', RegistrationView.as_view(), name='accounts_registration'),
    url(r'^fb-auth/$', FacebookLoginView.as_view(), name='accounts_fb_login'),
    url(r'^google-auth/$', GoogleLoginView.as_view(), name='accounts_google_login'),
]
