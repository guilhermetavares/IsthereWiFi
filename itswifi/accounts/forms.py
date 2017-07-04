# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class LoginForm(AuthenticationForm):
    username = forms.EmailField()
    password = forms.CharField()


class RegistrationForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('password', 'email', 'name')
