# -*- coding: utf-8 -*-
from django import forms

from .models import Establishment, EstablishmentEvaluation


class EstablishmentForm(forms.ModelForm):
	
	class Meta:
		model = Establishment
		fields = ('name', 'address', 'city', 'address', 'state', 'country', 'category')


class EstablishmentEvaluationForm(forms.ModelForm):
    class Meta:
        model = EstablishmentEvaluation
        exclude = ('user', 'establishment')
