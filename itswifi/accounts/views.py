# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic import FormView, View
from django.contrib.auth import authenticate, login as django_login

from .models import User
from .forms import LoginForm, RegistrationForm


class GoogleLoginView(View):

    def get(self, request, *args, **kwargs):      
        name = request.GET.get('name')
        email = request.GET.get('email')

        user = User.objects.filter(email=email).first()
        if user is None:
            user = User.objects.create(name=name, email=email)

        django_login(self.request, user)
        return redirect(self.request.GET.get('next', '/'))


class FacebookLoginView(View):
    BASE_FORMAT_EMAIL = '{0}@login.facebook.com.br'

    def get(self, request, *args, **kwargs):      
        name = request.GET.get('name')
        facebook = request.GET.get('facebook')
        email = self.BASE_FORMAT_EMAIL.format(facebook)

        user = User.objects.filter(email=email).first()
        if user is None:
            user = User.objects.create(name=name, email=email)

        django_login(self.request, user)
        return redirect(self.request.GET.get('next', '/'))


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        context['YOUR_CLIENT_ID'] = ''
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
