from django import forms

from product_output.forms import ProductOutputForm
from .models import Order
from googletrans import Translator


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        translator = Translator()
        labels = list()

        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            labels.append(value.label)

        string_to_translate = ' | '.join(labels)
        string_to_translate = translator.translate(string_to_translate, src='en', dest='pt').text
        string_to_translate = iter(string_to_translate.split(' |'))

        for key, value in self.fields.items():
            value.label = next(string_to_translate)

    class Meta:
        model = Order
        fields = ['client_id', 'selling_date', 'payment_form']


class InlineOrderProductForm(OrderForm, ProductOutputForm):
    pass
