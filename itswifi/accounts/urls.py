# -*- coding: utf-8 -*-
from .views import LoginView, RegistrationView
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='accounts_login'),
    url(r'^cadastre-se/$', RegistrationView.as_view(), name='accounts_registration'),
]
