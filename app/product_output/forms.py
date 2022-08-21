from django import forms

from product.models import Product
from .models import ProductOutput
from utils_global.translated_labels import product_output_labels

class ProductOutputModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})
            value.label = product_output_labels.get(value.label)

    class Meta:
        model = ProductOutput
        fields = ['order', 'product_id', 'quantity']

class ProductOutputForm(forms.Form):
    quantity = forms.IntegerField(required=True, label='Quantidade', min_value=1, max_value=2000000000)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Produto')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class': 'form-control'})

