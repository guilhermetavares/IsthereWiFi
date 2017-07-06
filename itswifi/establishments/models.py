# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db import models

from localflavor.br.models import BRStateField


class Establishment(models.Model):
    ESTABLISHMENT_CATEGORY = (
        (1, _('Café')),
        (2, _('Restaurante')),
        (3, _('Coworking')),
        (4, _('Livraria')),
        (5, _('Outro')),
    )
    name = models.CharField(_('Nome'), max_length=250)
    address = models.CharField(_('Endereço'), max_length=250)
    city = models.CharField(_('Cidade'), max_length=64)
    address = models.CharField(_('Endereço'), max_length=250)
    state = BRStateField(_('Estado'))
    country = models.CharField(_('País'), max_length=50)
    category = models.IntegerField(_('Tipo'), default=1, choices=ESTABLISHMENT_CATEGORY)

    def get_absolute_url(self):
        return reverse('establishments_detail', args=[self.pk,])


class EstablishmentEvaluation(models.Model):
    user = models.ForeignKey(u'accounts.User')
    establishment = models.ForeignKey(Establishment, related_name='evaluates')

    foods = models.TextField()
    drinks = models.TextField()

    internet_password = models.CharField(max_length=50)
    internet_open = models.IntegerField()
    internet_rating = models.IntegerField()

    customer_service = models.IntegerField()
    price = models.IntegerField()
    comfortable = models.IntegerField()
    noise = models.IntegerField()
    geral = models.IntegerField()
