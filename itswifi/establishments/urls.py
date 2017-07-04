# -*- coding: utf-8 -*-
from .views import EstablishmentListView, EstablishmentDetailView, EstablishmentEvaluateView
from django.conf.urls import url


urlpatterns = [
    url(r'^estabelecimentos/$', EstablishmentListView.as_view(), name='establishments_list'),
    url(r'^estabelecimentos/(?P<slug>[\w-]+)/$', EstablishmentDetailView.as_view(), name='establishments_detail'),
    url(r'^estabelecimentos/(?P<slug>[\w-]+)/evaluate/$', EstablishmentEvaluateView.as_view(), name='establishments_evaluate'),
]
