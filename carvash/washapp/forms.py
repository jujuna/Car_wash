from django import forms
from .models import Car
from django.forms import ModelChoiceField

class CarForm(forms.ModelForm):
    

    class Meta:
        model=Car
        fields="__all__"