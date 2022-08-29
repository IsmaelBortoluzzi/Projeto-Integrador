import datetime

from django.forms import ModelForm, TextInput, HiddenInput, DateField, Select
from .models import Order
from utils_global.translated_labels import order_labels

class OrderForm(ModelForm):

    selling_date = DateField(widget=TextInput(attrs={'type':'date'}), initial= datetime.date.today, label='Selling date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = order_labels.get(value.label)

    class Meta:
        model = Order
        fields = ['client_id', 'selling_date']
        widgets = {
            'selling_date': TextInput(attrs={'type':'date'}),
        }

class OrderPaymentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = order_labels.get(value.label)

    class Meta:
        model = Order
        fields = '__all__'
        PAYMENT_CHOICES = (
            ('', 'Selecione a forma de pagamento'),
            ('DI', 'Dinheiro'),
            ('CC', 'Cartão de Crédito'),
            ('CD', 'Cartão de Débito'),
            ('PI', 'PIX'),
            ('OU', 'Outros'),
        )
        widgets = {
            'payment_form': Select(choices=PAYMENT_CHOICES,attrs={'class': 'form-control'}),
            'selling_date': HiddenInput(),
            'client_id': HiddenInput(),
            'is_active': HiddenInput(),
        }