# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import logout as django_logout

from .views import GoogleLoginView, LogOutView, LoginView, RegistrationView, FacebookLoginView

urlpatterns = [
    url(r'^logout/$', LogOutView.as_view(), name='accounts_logout'),
    url(r'^login/$', LoginView.as_view(), name='accounts_login'),
    url(r'^cadastre-se/$', RegistrationView.as_view(), name='accounts_registration'),
    url(r'^fb-auth/$', FacebookLoginView.as_view(), name='accounts_fb_login'),
    url(r'^google-auth/$', GoogleLoginView.as_view(), name='accounts_google_login'),
]
