import datetime
from django import forms


class SupplierForm(forms.Form):
    corporate_name = forms.CharField(max_length=128, required=True, label='Razão Social ')
    fantasy_name = forms.CharField(max_length=128, required=False, label='Nome Fantasia')
    cnpj = forms.CharField(max_length=14, label='cnpj', required=True)
    email = forms.EmailField(label='email', required=False)
    phone_number = forms.CharField(max_length=32, required=False, label='telefone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if not self.cleaned_data.get('cnpj').isdigit():
            raise forms.ValidationError('CNPJ deve conter somente dígitos!')

        return self.cleaned_data
