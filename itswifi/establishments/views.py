# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView

from common.cbv import LoginRequiredMixin

from .models import Establishment


class EstablishmentListView(ListView):
	template_name = 'establishments/list.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			return Establishment.objects.filters(name__icontains=self.request.GET.get('q'))
		return Establishment.objects.all()



class EstablishmentDetailView(DetailView):
	template_name = 'establishments/detail.html'
	model = Establishment



class EstablishmentEvaluateView(LoginRequiredMixin, FormView):
	template_name = 'establishments/detail.html'
	model = Establishment

