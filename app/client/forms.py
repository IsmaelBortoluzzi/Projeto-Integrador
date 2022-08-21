import datetime

from django import forms


class ClientForm(forms.Form):
    full_name = forms.CharField(max_length=128, label='Nome')
    nickname = forms.CharField(max_length=128, label='Apelido', required=False)
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}), initial= datetime.date.today, label='Data de nascimento', required=False)
    cpf = forms.CharField(max_length=11, label='CPF')
    phone_number = forms.CharField(max_length=32, required=False, label='Número de Telefone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if not self.cleaned_data.get('cpf').isdigit():
            raise forms.ValidationError('CPF deve conter somente dígitos!')
            
        return self.cleaned_data


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
