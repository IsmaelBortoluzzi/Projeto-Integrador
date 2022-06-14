import datetime

from django import forms


class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=128, label='Nome')
    nickname = forms.CharField(max_length=128, label='Apelido', required=False)
    birth_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'placeholder': '__/__/____',
        },
            format='%d/%m/%Y',
        )
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
