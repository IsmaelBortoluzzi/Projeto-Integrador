import datetime

from django import forms


class ClientForm(forms.Form):
    full_name = forms.CharField(max_length=128, label='Nome')
    nickname = forms.CharField(max_length=128, label='Apelido', required=False)
    birth_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'placeholder': '__/__/____',
        },
            format='%d/%m/%Y',
        ),
        required=False
    )
    cpf = forms.CharField(max_length=11, label='CPF')
    phone_number = forms.CharField(max_length=32, required=False, label='Número de Telefone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if not self.cleaned_data.get('cpf').isdigit():
            raise forms.ValidationError('CPF deve conter somente dígitos!')

        birth_date = self.cleaned_data.get('birth_date')

        if birth_date is None:
            return self.cleaned_data

        # converts date format into DB date pattern
        self.cleaned_data.update(
            {
                'birth_date': datetime.datetime.strptime(birth_date.strftime('%Y-%m-%d'), '%Y-%m-%d')
            }
        )
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
