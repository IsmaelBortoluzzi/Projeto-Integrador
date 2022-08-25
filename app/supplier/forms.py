import datetime

from django import forms


class SupplierForm(forms.Form):
    corporate_name = forms.CharField(max_length=128, required=True, label='Razão Social ')
    fantasy_name = forms.CharField(max_length=128, required=False, label='Nome Fantasia')
    created = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}), initial= datetime.date.today, label='Data da criação', required=False)
    cnpj = forms.CharField(max_length=14, label='CNPJ', required=True)
    email = forms.EmailField(label='Email', required=False)
    phone_number = forms.CharField(max_length=32, required=False, label='Telefone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if not self.cleaned_data.get('cnpj').isdigit():
            raise forms.ValidationError('CNPJ deve conter somente dígitos!')

        return self.cleaned_data
