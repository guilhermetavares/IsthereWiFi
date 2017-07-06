# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from datetime import datetime


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('Nome'), max_length=50)
    email = models.EmailField(unique=True)
    create_at = models.DateTimeField(_('Criado em'), default=datetime.now)
    USERNAME_FIELD = 'email'

    objects = UserManager()
    REQUIRED_FIELDS = ['name', ]

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email