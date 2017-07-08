# -*- coding: utf-8 -*-
from django import forms

from .models import Establishment, EstablishmentEvaluation


class EstablishmentForm(forms.ModelForm):
	
	class Meta:
		model = Establishment
		exclude = ('create_at', )


class EstablishmentEvaluationForm(forms.ModelForm):
    class Meta:
        model = EstablishmentEvaluation
        exclude = ('user', 'establishment', 'create_at')
