# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login as django_login

from .forms import LoginForm, RegistrationForm


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

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
