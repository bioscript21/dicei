from django import forms
from django.forms import ModelForm
from .models import *


class IncluidoForm(ModelForm):

    class Meta:
        model = Incluido
        fields = '__all__'

        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'iniciales': forms.TextInput(attrs={'class': 'form-control'}),
            'feceva': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'inclusion': forms.RadioSelect(attrs={'class': 'form-control'}),
            'fecinc': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'causano': forms.NumberInput(attrs={'class': 'form-control'}),
            'investigador': forms.TextInput(attrs={'class': 'form-control'}),
            'firma': forms.RadioSelect(attrs={'class': 'form-control'}),
        }


class RecDevPiForm(ModelForm):

    class Meta:
        model = RecDevPi
        fields = '__all__'

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_1': forms.TextInput(attrs={'class': 'form-control'}),
            'entrega_1': forms.TextInput(attrs={'class': 'form-control'}),
            'recibe_1': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'codigo_2': forms.TextInput(attrs={'class': 'form-control'}),
            'entrega_2': forms.TextInput(attrs={'class': 'form-control'}),
            'recibe_2': forms.TextInput(attrs={'class': 'form-control'}),
        }
