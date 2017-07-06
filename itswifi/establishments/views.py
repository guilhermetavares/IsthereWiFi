# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView

from common.cbv import LoginRequiredMixin

from .models import Establishment
from .forms import EstablishmentForm, EstablishmentEvaluationForm


class EstablishmentListView(ListView):
    template_name = 'establishments/list.html'

    def get_queryset(self):
        if self.request.GET.get('q'):
            return Establishment.objects.filters(name__icontains=self.request.GET.get('q'))
        return Establishment.objects.all()



class EstablishmentDetailView(DetailView):
    template_name = 'establishments/detail.html'
    model = Establishment

    def get_context_data(self, *args, **kwargs):
        context = super(EstablishmentDetailView, self).get_context_data(*args, **kwargs)
        context['form'] = getattr(self, 'form', EstablishmentEvaluationForm())
        return context

    def post(self, request, *args, **kwargs):      
        form = EstablishmentEvaluationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.establishment = self.get_object()
            instance.save()
        else:
            self.form = form
        return super(EstablishmentDetailView, self).get(request, *args, **kwargs)


class EstablishmentEvaluateView(LoginRequiredMixin, FormView):
    template_name = 'establishments/detail.html'
    model = Establishment


class EstablishmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'establishments/create.html'
    model = Establishment
    form_class = EstablishmentForm
    success_url = ''