# -*- coding: utf-8 -*-
from django.views.generic import View
from django.utils.http import urlquote
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


class LoginRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('{0}?next={1}'.format(reverse('accounts_login'), urlquote(request.get_full_path())))
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
