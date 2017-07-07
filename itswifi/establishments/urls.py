# -*- coding: utf-8 -*-
from .views import EstablishmentCreateView, EstablishmentListView, EstablishmentDetailView, EstablishmentEvaluateView
from django.conf.urls import url


urlpatterns = [
    url(r'^avaliacoes/$', EstablishmentListView.as_view(), name='establishmentevaluate_list'),

    url(r'^estabelecimentos/$', EstablishmentListView.as_view(), name='establishments_list'),
    url(r'^estabelecimentos/add/$', EstablishmentCreateView.as_view(), name='establishments_create'),
    url(r'^estabelecimentos/(?P<pk>[\w-]+)/$', EstablishmentDetailView.as_view(), name='establishments_detail'),
    url(r'^estabelecimentos/(?P<slug>[\w-]+)/evaluate/$', EstablishmentEvaluateView.as_view(), name='establishments_evaluate'),
]
