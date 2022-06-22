from django import forms
from dal import autocomplete

from supplier.models import Supplier


class BrandForm(forms.Form):
    name = forms.CharField(max_length=255, label='Nome', required=True)
    initials = forms.CharField(max_length=16, label='Iniciais', required=False)  # sigla
    supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        widget=autocomplete.ModelSelect2(url='supplier-autocomplete'),
        label='Fornecedor',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if not self.cleaned_data.get('Nome'):
            raise forms.ValidationError('Nome não pode estar vazio!')
