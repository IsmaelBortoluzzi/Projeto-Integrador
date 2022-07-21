from django import forms

from product.models import Product
from googletrans import Translator
from utils_global.translated_labels import product_form_labels


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # translator = Translator()
        for key, value in self.fields.items():  # pra cada campo, adiciona a classe bootstrap form-control
            value.widget.attrs.update({'class': 'form-control'})
            # value.label = translator.translate(value.label, src='en', dest='pt').text
            value.label = product_form_labels.get(value.label)

    class Meta:
        model = Product
        fields = [
                'name', 'barcode', 'selling_price', 'brand', 'product_category',
                'description', 'is_active', 'profit_margin',
                'current_inventory','minimum_inventory'
            ]
