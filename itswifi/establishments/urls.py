# -*- coding: utf-8 -*-
from .views import EstablishmentCreateView, EstablishmentListView, EstablishmentDetailView, EstablishmentEvaluateListView
from django.conf.urls import url


urlpatterns = [
    url(r'^avaliacoes/$', EstablishmentEvaluateListView.as_view(), name='establishmentevaluate_list'),
    url(r'^estabelecimentos/$', EstablishmentListView.as_view(), name='establishments_list'),
    url(r'^estabelecimentos/add/$', EstablishmentCreateView.as_view(), name='establishments_create'),
    url(r'^estabelecimentos/(?P<pk>[\w-]+)/$', EstablishmentDetailView.as_view(), name='establishments_detail'),
]
