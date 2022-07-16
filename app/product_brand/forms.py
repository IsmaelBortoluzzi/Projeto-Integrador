from django import forms
from dal import autocomplete

from supplier.models import Supplier


class BrandForm(forms.Form):
    name = forms.CharField(max_length=255, label='Nome', required=True)
    initials = forms.CharField(max_length=16, label='Iniciais', required=False)  # sigla

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})


class BrandEditForm(forms.Form):
    name = forms.CharField(max_length=255, label='Nome', required=True)
    initials = forms.CharField(max_length=16, label='Iniciais', required=False)  # sigla

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})