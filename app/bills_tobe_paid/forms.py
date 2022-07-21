from django import forms

from bills_tobe_paid.models import BillsToBePaid
from product.models import Product
from googletrans import Translator
from utils_global.translated_labels import product_form_labels


class BillsToBePaidForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        translator = Translator()
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})
            value.label = translator.translate(value.label, src='en', dest='pt').text
            # value.label = product_form_labels.get(value.label)

    class Meta:
        model = BillsToBePaid
        fields = '__all__'
