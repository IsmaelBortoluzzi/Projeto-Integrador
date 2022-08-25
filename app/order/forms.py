import datetime

from django.forms import ModelForm, TextInput, HiddenInput, DateField
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
        widgets = {
            'selling_date': HiddenInput(),
            'client_id': HiddenInput(),
            'is_active': HiddenInput(),
        }