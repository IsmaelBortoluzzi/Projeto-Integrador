from django import forms


class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=128, label='Nome')
    nickname = forms.CharField(max_length=128, label='Apelido', required=False)
    birth_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    cpf = forms.CharField(max_length=11, label='CPF')
    phone_number = forms.CharField(max_length=32, required=False, label='Número de Telefone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        if not self.cleaned_data.get('cpf').isdigit():
            raise forms.ValidationError('CPF deve conter somente dígitos!')



