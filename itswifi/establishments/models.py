# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

from localflavor.br.models import BRStateField

from common.fields import IntegerRangeField

class Establishment(models.Model):
    ESTABLISHMENT_CATEGORY = (
        (1, _('Café')),
        (2, _('Restaurante')),
        (3, _('Coworking')),
        (4, _('Livraria')),
        (5, _('Outro')),
    )
    category = models.IntegerField(_('Tipo'), default=1, choices=ESTABLISHMENT_CATEGORY)
    name = models.CharField(_('Nome'), max_length=250)

    zip_code = models.CharField(_('CEP'), max_length=10)
    number = models.IntegerField(_('Número'))
    address = models.CharField(_('Endereço'), max_length=250)
    city = models.CharField(_('Cidade'), max_length=64)
    address = models.CharField(_('Endereço'), max_length=250)
    state = BRStateField(_('Estado'))
    country = models.CharField(_('País'), max_length=50)
    
    create_at = models.DateTimeField(_('Criado em'), default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('establishments_detail', args=[self.pk,])


class EstablishmentEvaluation(models.Model):

    user = models.ForeignKey(u'accounts.User')
    establishment = models.ForeignKey(Establishment, related_name='evaluates')

    internet_password = models.CharField(_('Possui Internet? Ela possui senha? Qual?'), max_length=50)
    internet_rating = IntegerRangeField(_('Avalie a Internet'), min_value=0, max_value=5)

    foods = models.TextField(_('Descreva os tipos de comidas são servidos?'))
    drinks = models.TextField(_('Descreva os tipos de bebidas são servidos?'))

    customer_service = IntegerRangeField(_('Avalie o Atendimento'), min_value=1, max_value=5)
    price = IntegerRangeField(_('Avalie o Preço'), min_value=1, max_value=5)
    comfortable = IntegerRangeField(_('Avalie o Espaço'), min_value=1, max_value=5)
    noise = IntegerRangeField(_('Avalie o Barulho'), min_value=1, max_value=5)
    geral = IntegerRangeField(_('Avaliação Geral'), min_value=1, max_value=5)

    create_at = models.DateTimeField(_('Criado em'), default=timezone.now)
    
    class Meta:
        ordering = ('-create_at', 'geral')
