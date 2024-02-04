from django import forms
from .models import *


class CarForm(forms.Form):
    name = forms.CharField(max_length=100, label='Введите марку авто')


class CarTypeForm(forms.Form):
    name = forms.CharField(max_length=100, label='Введите тип авто')
                           # attrs={'class': 'form-control'})
    widget = forms.TextInput(attrs={'class': 'form-control', 'label': 'Тип автомобиля'})

class Car_all(forms.Form):
    car_number = forms.CharField(max_length=10, label='Введите гос номер авто')
    year = forms.IntegerField(label='Введите год выпуска авто')
    is_electric = forms.BooleanField(label='Электропривод', required=False)
