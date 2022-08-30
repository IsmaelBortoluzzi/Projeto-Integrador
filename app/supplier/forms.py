import datetime

from django import forms
from .models import Supplier
from utils_global.translated_labels import supplier_labels


class SupplierForm(forms.ModelForm):
    corporate_name = forms.CharField(max_length=128, required=True, label='Corporate name')
    fantasy_name = forms.CharField(max_length=128, required=False, label='Fantasy name')
    created = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}), initial= datetime.date.today, label='Created', required=False)
    cnpj = forms.CharField(max_length=14, label='Cnpj', required=True)
    email = forms.EmailField(label='Email', required=False)
    phone_number = forms.CharField(max_length=32, required=False, label='Phone number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = supplier_labels.get(value.label)

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if not cnpj.isdigit():
            raise forms.ValidationError('CNPJ deve conter somente dígitos!')
        if not len(cnpj) == 14:
            raise forms.ValidationError('CNPJ deve ter exatamente 11 dígitos!')
        try:
            match = Supplier.objects.get(cnpj=cnpj)
            if match.pk == self.instance.pk:
                return cnpj
            else:
                raise forms.ValidationError('CNPJ utilizado em outro cadastro!')
        except Supplier.DoesNotExist:
            return cnpj

    class Meta:
        model = Supplier
        fields = '__all__'
