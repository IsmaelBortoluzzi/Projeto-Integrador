import datetime

from django import forms
from .models import Client
from utils_global.translated_labels import client_labels

class ClientForm(forms.ModelForm):
    full_name = forms.CharField(max_length=128, label='Full name')
    nickname = forms.CharField(max_length=128, label='Nickname', required=False)
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}), initial= datetime.date.today, label='Birth date', required=False)
    cpf = forms.CharField(max_length=11, label='Cpf')
    phone_number = forms.CharField(max_length=32, required=False, label='Phone number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = client_labels.get(value.label)

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not cpf.isdigit():
            raise forms.ValidationError('CPF deve conter somente dígitos!')
        if not len(cpf) == 11:
            raise forms.ValidationError('CPF deve ter exatamente 11 dígitos!')
        try:
            match = Client.objects.get(cpf=cpf)
            if match.pk == self.instance.pk:
                return cpf
            else:
                raise forms.ValidationError('CPF utilizado em outro cadastro!')
        except Client.DoesNotExist:
            return cpf

    class Meta:
        model = Client
        fields = '__all__'


class AddressForm(forms.Form):

    STATE_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )

    cep = forms.CharField(max_length=8, label='CEP', required=False)
    street = forms.CharField(max_length=256, label='Rua', required=False)
    number = forms.IntegerField(label='Número', required=False)
    district = forms.CharField(max_length=256, label='Bairro', required=False)
    city = forms.CharField(max_length=256, label='Cidade', required=False)
    state = forms.ChoiceField(choices=STATE_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if not self.cleaned_data.get('cep').isdigit():
            raise forms.ValidationError('CEP deve conter somente dígitos!')
