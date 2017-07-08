# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, View
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate, login as django_login

from .models import User
from .forms import LoginForm, RegistrationForm


class LogOutView(View):

    def get(self, request, *args, **kwargs):
        django_logout(request)
        return redirect('/')


class GoogleLoginView(View):

    def get(self, request, *args, **kwargs):
        email = request.GET.get('email')

        user = User.objects.filter(email=email).first()
        if user is None:
            return redirect('accounts_registration')

        django_login(self.request, user)
        return redirect(self.request.GET.get('next', '/'))


class FacebookLoginView(View):
    BASE_FORMAT_EMAIL = '{0}@login.facebook.com.br'

    def get(self, request, *args, **kwargs):      
        email = request.GET.get('email')

        user = User.objects.filter(email=email).first()
        if user is None:
            return redirect('accounts_registration')

        django_login(self.request, user)
        return redirect(self.request.GET.get('next', '/'))


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        return context

    def form_valid(self, form):
        user = form.get_user()
        django_login(self.request, user)
        return redirect(self.request.GET.get('next', '/'))


class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        user = form.save()
        django_login(self.request, user)
        return redirect('/')
